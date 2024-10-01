import os
import pandas as pd
from glob import glob

class DataLoader:
    def __init__(self, data_directory):
        self.data_directory = data_directory
        self.file_paths = []
        self.data = pd.DataFrame()

    def load_data(self):
        # Get all CSV file paths
        self.file_paths = glob(os.path.join(self.data_directory, '*.csv'))
        dataframes = []  # List to hold individual DataFrames
        for file_path in self.file_paths:
            try:
                df = pd.read_csv(file_path)
                dataframes.append(df)  # Add DataFrame to the list
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

        # Concatenate all DataFrames into one
        if dataframes:
            self.data = pd.concat(dataframes, ignore_index=True)
        else:
            print("No CSV files found or all files failed to load.")

    def save_read_data(self, output_file):
        """
        Saves the combined data to a CSV file.

        :param output_file: The path to save the combined data.
        """
        if not self.data.empty:
            self.data.to_csv(output_file, index=False)
            print(f"Combined data saved to '{output_file}'.")
        else:
            print("No data to save.")

def main():
    data_loader = DataLoader(data_directory='data')
    data_loader.load_data()
    data_loader.save_read_data('ctg_data.csv')

if __name__ == '__main__':
    main()
