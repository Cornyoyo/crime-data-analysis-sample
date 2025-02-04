import pandas as pd

# --- Project: Simple Crime Data Analysis ---
# This script analyzes Chicago crime data to demonstrate basic data analysis skills.
# It performs several tasks:
#   Task A: Counts the frequency of different crime types.
#   Task B: Counts crimes by community area.
#   Task C: Filters crimes by a specific type and community area.
#   Task D: Counts crimes by day of the week.
#   Task E: Analyzes crime trends over time (monthly).

# --- Load Crime Data from CSV file ---
try:
    crime_data = pd.read_csv("crimes.csv")  
    print("Data loaded successfully from 'crimes.csv'")
except FileNotFoundError:
    print("Error: crimes.csv not found. Please ensure the file is in the same directory.")
    exit()
print("--- End Data Loading ---")


# --- Initial Data Inspection ---
print("\n--- Initial Data Inspection ---")
print("\nFirst 5 rows of the dataset:")
print(crime_data.head())
print("\nDataset information (column names, data types, non-null counts):")
print(crime_data.info())
print("\nSummary statistics for numerical columns:")
print(crime_data.describe())
print("--- End Initial Data Inspection ---")


# --- Data Cleaning ---
# Handling missing values in 'Community Area'
print("\n--- Data Cleaning: Handling Missing Community Area Values ---")
print(f"Number of missing values in 'Community Area' column before cleaning: {crime_data['Community Area'].isnull().sum()}")
crime_data['Community Area'] = crime_data['Community Area'].fillna(0) 
print(f"Number of missing values in 'Community Area' column after filling with 0: {crime_data['Community Area'].isnull().sum()}")
print("--- End Data Cleaning: Missing Community Area Values ---")
# --- End Data Cleaning ---


# --- Task A: Analyze Crime Type Counts ---
# We want to understand the distribution of different types of crimes reported.
crime_type_counts = crime_data['Primary Type'].value_counts()
print("\n--- Task A: Top 10 Most Frequent Crime Types ---")
print(f"Displaying the top 10 most frequent 'Primary Type' crimes in the dataset:\n")
print(crime_type_counts.head(10))
print("--- End Top 10 Crime Types ---")


# --- Task B: Analyze Crimes by Community Area ---
# To understand crime distribution geographically, we count crimes per community area.
community_crime_counts = crime_data['Community Area'].value_counts()
print("\n--- Task B: Top 10 Community Areas with Highest Crime Counts ---")
print(f"Displaying the top 10 community areas with the highest number of reported crimes:\n")
print(community_crime_counts.head(10))
print("--- End Top 10 Community Areas ---")


# --- Task C: Filter and Analyze Specific Crime Type in a Community Area ---
specific_crime_type = "THEFT" 
specific_community_area = 25 
print(f"\n--- Task C: Analyzing '{specific_crime_type}' Crimes in Community Area {specific_community_area} ---")
filtered_crimes = crime_data[
    (crime_data['Primary Type'] == specific_crime_type) & 
    (crime_data['Community Area'] == specific_community_area) 
]
num_filtered_crimes = len(filtered_crimes)
print(f"Number of '{specific_crime_type}' crimes reported in Community Area {specific_community_area}: {num_filtered_crimes}")
print(f"Details of the first few '{specific_crime_type}' crimes in Community Area {specific_community_area}:\n")
print(filtered_crimes.head()) # Show a few examples of the filtered crimes
print(f"--- End Analysis of '{specific_crime_type}' Crimes in Community Area {specific_community_area} ---")


# --- Task D: Analyze Crimes by Day of the Week ---
# To understand crime patterns, we analyze crime frequency by day of the week.
print("\n--- Task D: Analyzing Crimes by Day of the Week ---")

crime_data['Date'] = pd.to_datetime(crime_data['Date'], format='%m/%d/%Y %I:%M:%S %p') # Convert date strings to datetime objects using specific format
crime_data['Day of Week'] = crime_data['Date'].dt.day_name() # Create 'Day of Week' column
day_of_week_counts = crime_data['Day of Week'].value_counts()
print(f"Frequency of crimes by day of the week:\n")
print(day_of_week_counts)
print("--- End Analysis of Crimes by Day of the Week ---")

# --- Task E: Crimes Over Time (Monthly Trend) ---
print("\n--- Task E: Crimes Over Time (Monthly Trend) ---")

# Set Date as index and calculate monthly counts
crime_data = crime_data.set_index('Date')
monthly_crime_counts = crime_data.resample('ME').size()

print("\nMonthly Crime Counts:")
print(monthly_crime_counts)

print("\nMonthly Crime Counts (Formatted):")
for month, count in monthly_crime_counts.items():
    print(f"{month.strftime('%Y-%m')}: {count} crimes")


print("\n--- End of Crime Data Analysis Script ---")