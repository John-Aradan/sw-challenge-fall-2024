# CTG Stock Data Processing Pipeline

## Introduction

In Quantitative Finance, data is everything. This project simulates the task of loading, cleaning, and transforming historical high-frequency tick data for a fictional stock "CTG". It involves processing tick data into OHLCV bars (Open, High, Low, Close, Volume) over user-specified time intervals, using object-oriented programming principles.

## Task Overview

This project consists of three primary components:

1. **Data Loading**: Efficiently load and combine thousands of CSV files containing tick data.
2. **Data Cleaning**: Identify and address four consistent data issues.
3. **Data Transformation**: Provide an interface to generate OHLCV bars over specified time intervals.

## Context

Handling high-frequency tick data is essential in quantitative finance for trading strategy development. This project focuses on:

- **Data Handling**: Efficient loading and processing of large datasets.
- **Data Integrity**: Cleaning raw tick data to ensure accuracy.
- **Time Series Analysis**: Aggregating data into OHLCV bars, a common format in financial analysis.

## Requirements

The task is completed using core Python libraries without external dependencies. You should be able to execute the provided Python code and generate the expected outputs without additional installations.

### 1. Data Loading

This module reads thousands of CSV files, combines them into one, and stores them for further processing.

#### Key Features:

- **Efficient File Reading**: Handles large numbers of CSV files.
- **Error Handling**: Gracefully manages file reading errors.

### 2. Data Cleaning

The cleaning module processes the tick data by identifying four data issues:

- Dropping rows with missing values.
- Removing rows with negative prices.
- Filtering out price outliers (outside the range 400-450).
- Removing duplicate rows.

#### Key Features:

- **Data Validation**: Ensures no missing values or invalid prices.
- **Anomaly Detection**: Detects outliers and invalid data points.
- **Visualization**: Basic plotting for feature distributions (optional).
![Plotting Price Column](Images/WhatsApp%20Image%202024-09-30%20at%2023.43.57_cc1850ba.jpg)


### 3. Data Transformation (OHLCV Generator)

The transformation module generates OHLCV bars for specified time intervals and date ranges.

#### Key Features:
- **Flexible Interval Parsing**: Supports complex time intervals such as "15m", "1h30m", etc.
- **OHLCV Calculation**: Calculates Open-High-Low-Close-Volume bars from the tick data.
- **File Output**: Saves aggregated data to CSV files.

## Assumptions & Limitations

- **Time Intervals**: Accepted in formats like "4s", "15m", "1h", etc.
- **Error Handling**: Basic error handling is included, but advanced validation could be extended.
- **Data Validation**: The program assumes valid input data and performs minimal validation.

## Conclusion

This project demonstrates core principles of data processing in quantitative finance, focusing on:

- **Data Cleaning**: Addressing common issues with high-frequency tick data.
- **Data Transformation**: Generating OHLCV data for analysis.
- **Object-Oriented Programming**: Modular and extensible design for future applications.
