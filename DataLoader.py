"""

Notes:
    
I chose to split into 3 files due to the following reasons:
    1. It was easier to split the problem into three parts
    2. Incase one for another project we may need just want one part this split might be helpful

My record on how I approached the problem:
    
    Given that it is required to demonstrate OOP principles, I started by creating 
    a class called DataLoader
    
    Since there were only 2 tasks that are required to be done which were (i) to combine 
    and load all the seperate csv files and (ii) save it as a seperate csv file so that it would be eaiser to acccess it for future operations.
    
    So I created 2 functions load_data and save_read_data as instance functions to perform these operations
    
"""

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
