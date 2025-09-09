# uber-data_analytics

**Project Overview**
This script, written in Python, demonstrates a comprehensive data wrangling workflow for Uber ride bookings data. It provides steps for missing value imputation, categorical value mapping, and date-time processing—crucial phases in a real-world machine learning or analytics pipeline.

Main Features
Data Loading & Exploration

Loads the dataset with Pandas and previews its structure and missing data.

Missing Data Handling

Fills missing numeric values with column means using SimpleImputer.

Replaces missing values in specific columns with defaults (e.g., 0 for cancellation counts, 'Unknown' for reasons).

Categorical Feature Engineering

Encodes categorical features like booking status, vehicle type, payment method, and cancellation reasons into numeric codes using mapping.

Date-Time Processing

Converts and combines separate date and time columns into a single datetime column for better temporal analysis.

Exploratory Steps

Shows value counts, statistical summaries, and a correlation heatmap for initial exploration.

Technologies Used
Python (with NumPy and Pandas)

Seaborn (for visualization)

Scikit-learn (for imputation)

Usage
Ensure the dataset (ncr_ride_bookings.csv) is available in the correct directory.

Run the script to:

Preprocess, clean, and encode data, making it ready for further analytics or modeling.

View exploratory results and formatted data output.

Suitable For
Data scientists and analysts preparing ride bookings data for analysis or machine learning.

Learners practicing feature engineering and preprocessing with real-world datasets.


