import pandas as pd
import warnings
import re
from datetime import datetime, timedelta

warnings.filterwarnings("ignore", category=pd.errors.SettingWithCopyWarning)


class DataOHLVC:
    def __init__(self):
        self.data = pd.DataFrame()

    def load_data(self):
        try:
            self.data = pd.read_csv("cleaned_ctg_data.csv")
        except Exception as e:
            print(f"Error reading file: {e}")
            
    def return_data(self):
        return self.data

    def validate_interval(self, interval):
        """Validates the time interval format."""
        pattern = r'^\d+[smhd](\d+[smhd])*$'
        if not re.match(pattern, interval):
            raise ValueError(f"Invalid time interval format: {interval}")

    def parse_interval(self, interval):
        """Parses a time interval string into a total seconds value."""
        total_seconds = 0
        matches = re.findall(r'(\d+)\s*([smhd])', interval)
        for value, unit in matches:
            value = int(value)
            if unit == 's':
                total_seconds += value
            elif unit == 'm':
                total_seconds += value * 60
            elif unit == 'h':
                total_seconds += value * 3600
            elif unit == 'd':
                total_seconds += value * 86400
        print (total_seconds)
        return total_seconds

    def generate_ohlcv(self, interval, start_time, end_time):
        """
        Generates OHLCV data for the specified time interval and range.
        """
        self.data['Timestamp'] = pd.to_datetime(self.data['Timestamp'])
        
        # Validate input
        self.validate_interval(interval)
        start_time = pd.to_datetime(start_time)
        end_time = pd.to_datetime(end_time)

        # Create an empty DataFrame for OHLCV data
        ohlcv_data = []

        # Set the interval in seconds
        interval_seconds = self.parse_interval(interval)

        # Resample the data based on the specified interval
        current_time = start_time
        while current_time < end_time:
            next_time = current_time + timedelta(seconds=interval_seconds)
            interval_data = self.data[(self.data['Timestamp'] >= current_time) & 
                                       (self.data['Timestamp'] < next_time)]

            if not interval_data.empty:
                open_price = interval_data.iloc[0, 2]  # First price in interval
                high_price = interval_data.iloc[:, 2].max()  # Highest price in interval
                low_price = interval_data.iloc[:, 2].min()  # Lowest price in interval
                close_price = interval_data.iloc[-1, 2]  # Last price in interval
                volume = interval_data.iloc[:, -1].sum()  # Total volume in interval

                ohlcv_data.append([current_time, open_price, high_price, low_price, close_price, volume])

            current_time = next_time

        # Convert the list of OHLCV data to a DataFrame
        ohlcv_df = pd.DataFrame(ohlcv_data, columns=['Timestamp', 'open', 'high', 'low', 'close', 'volume'])
        return ohlcv_df
    
    def save_ohlvc_data(self, ohlcv_df, output_file):
        ohlcv_df.to_csv(output_file, index=False)
    
def main():
    data_ohlvc = DataOHLVC()
    data_ohlvc.load_data()
    print("Successfully loaded data")
    
    interval = "4s"  # Time interval
    start_time = "2024-09-16 09:30:00.076"  # Start datetime
    end_time = "2024-09-16 09:36:20"  # End datetime

    try:
        ohlcv_data = data_ohlvc.generate_ohlcv(interval, start_time, end_time)
        print("OHLCV data generated")
    except ValueError as e:
        print(e)
    
    data_ohlvc.save_ohlvc_data(ohlcv_data,'ohlvc_ctg_data.csv')
   
if __name__ == '__main__':
    main()