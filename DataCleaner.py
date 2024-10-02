"""

Notes:

My record on how I approached the problem:
    
    Given that it is required to demonstrate OOP principles, I started by creating 
    a class called DataCleaner
    
    There were 3 tasks that are required to be done which were (i) load the data from the csv file, 
    (ii) to perfom operations on the data hece cleaning it and (iii) save it as a seperate csv file 
    so that it would be eaiser to acccess it for future operations.
    
    So I created 3 functions load_data,clean_data and save_cleaned_data as 
    instance functions to perform these operations
    
    I also created 2 more functions return_data, so I can analyze the loaded data 
    and determine what all cleaning process needs to be done and plot_data 
    so I could see the overall distribution of the data accross various features.
    
"""

import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore", category=pd.errors.SettingWithCopyWarning)


class DataCleaner:
    def __init__(self):
        self.data = pd.DataFrame()

    def load_data(self):
        try:
            self.data = pd.read_csv("ctg_data.csv")
        except Exception as e:
            print(f"Error reading file: {e}")
            
    def return_data(self):
        return self.data
    
    def plot_distribution(self, col):
        bins = range(0, 1100, 100)  # 0 to 1000 with an interval of 100
        labels = [f"{i}-{i+100}" for i in bins[:-1]]
        df = self.data.copy(deep=True)
        df['Binned'] = pd.cut(df[col], bins=bins, right=False, labels=labels)
        counts = df['Binned'].value_counts().sort_index()
        
        plt.figure(figsize=(10, 6))
        plt.plot(counts.index, counts.values, marker='o')
        plt.title(f'Distribution of {col}')
        plt.xlabel(f'{col} Range')
        plt.ylabel('Number of Entries')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
        plt.grid()
        plt.show()

    def clean_data(self):
        """
        Cleans the dataset by:
        1. Dropping rows with null or NaN values.
        2. Dropping rows with negative prices
        3. Removing duplicate rows.
        4. Filtering out outliers (price not in the range of 400-450).

        Updates the internal DataFrame with the cleaned data.
        """
        # 1. Drop rows with null or NaN values
        self.data.dropna(inplace=True)

        # 2. Drop rows where price (3rd column) is negative
        self.data = self.data[self.data.iloc[:, 1] >= 0]

        # 3. Remove duplicate rows
        self.data.drop_duplicates(inplace=True)

        # 4. Filter out outliers (price not in the range of 400-450)
        self.data = self.data[(self.data.iloc[:, 1] >= 400) & (self.data.iloc[:, 1] <= 450)]
        
        # 5. Convert timestamp to datetime
        self.data['Timestamp'] = pd.to_datetime(self.data['Timestamp'])

    def save_cleaned_data(self, output_file):
        """
        Saves the cleaned data to a CSV file.

        :param output_file: The path to save the cleaned data.
        """
        self.data.to_csv(output_file, index=False)

def main():
    data_cleaner = DataCleaner()
    data_cleaner.load_data()
    data_cleaner.plot_distribution("Price") # Size
    
    df = data_cleaner.return_data()
    
    print("Length od fatafreame before: ",len(df))
    null_rows = df.isnull().sum(axis=1)
    rows_with_nulls = null_rows[null_rows > 0].count()
    print("Number of rows with empty cells before: ", rows_with_nulls)
    count = df[(df.iloc[:,1] > 450) | (df.iloc[:,1] < 400)].shape[0]
    print("Ratio between outliers in price and total before :",count/len(df))
    
    data_cleaner.clean_data()
    print(df.head())
    
    df = data_cleaner.return_data()
    print("Length od fatafreame after: ",len(df))
    null_rows = df.isnull().sum(axis=1)
    rows_with_nulls = null_rows[null_rows > 0].count()
    print("Number of rows with empty cells after: ", rows_with_nulls)
    count = df[(df.iloc[:,1] > 450) | (df.iloc[:,1] < 400)].shape[0]
    print("Ratio between outliers in price and total after :",count/len(df))
    
    data_cleaner.save_cleaned_data('cleaned_ctg_data.csv')
   
if __name__ == '__main__':
    main()
    
