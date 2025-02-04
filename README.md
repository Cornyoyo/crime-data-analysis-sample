# Coding Sample: Chicago Crime Data Analysis - Basic Trends

This repository contains a Python script (`crime_analyzer.py`) that performs basic analysis on Chicago crime data from a CSV file. This code sample is submitted as part of my application for the Data Project Associate position at the University of Chicago Crime Ed Lab.

## Project Overview

This project aims to demonstrate my proficiency in analytic programming and data analysis using Python and Pandas, specifically in a context relevant to the University of Chicago Crime Lab's mission of using data to improve public safety.

The Python script `crime_analyzer.py` performs the following tasks on crime data:

*   **Task A: Crime Type Counts:**  Calculates and displays the frequency of different types of crimes reported in the dataset. This helps identify the most common crime categories.
*   **Task B: Crimes by Community Area:**  Determines and shows the number of crimes occurring in each community area. This provides insights into geographical crime distribution.
*   **Task C: Filtered Crime Count:**  Demonstrates the ability to filter the data to count crimes of a specific type within a specific community area. This shows targeted data querying.
*   **Task D: Crimes by Day of the Week:**  Analyzes crime patterns by day of the week to identify if certain days have higher crime frequencies.
*   **Task E: Crimes Over Time (Monthly Trend):**  Examines monthly crime trends throughout the year to understand how crime counts fluctuate over time.

These analyses provide a basic but informative overview of crime patterns within the dataset and demonstrate skills in data loading, manipulation, analysis, and presentation of results using Python and Pandas.

## How it Fits into a Larger Project

In a real-world crime analysis project at the University of Chicago Crime Ed Lab, this script could be a foundational component within a larger analytical workflow. For example, it could be:

*   **Part of an automated reporting system:**  The script could be scheduled to run regularly on updated crime data to generate routine reports on crime trends and patterns for policymakers and law enforcement agencies.
*   **A module within a larger data exploration dashboard:**  The results of these analyses could be integrated into an interactive dashboard to allow users to explore crime data in more detail and drill down into specific areas or crime types.
*   **A starting point for more advanced analyses:**  The script provides a basis for more sophisticated statistical modeling, predictive analysis, or spatial analysis of crime data.

## Technologies Used

*   **Python:** Chosen for its readability, versatility, and extensive libraries for data analysis. 
*   **Pandas:** A Python library specifically designed for data manipulation and analysis.

## Data Source

The script is designed to analyze crime data from a CSV file named `crimes.csv`. *The data was obtained from the City of Chicago Data Portal data.cityofchicago.org. A sample dataset is included in this repository for demonstration purposes.

## How to Run the Code

1.  **Prerequisites:** Ensure you have Python 3 and the Pandas library installed. 
2.  **Files:** Make sure `crime_analyzer.py` and `crimes.csv` are in the same directory.
3.  **Run from Terminal (macOS/Linux) or Command Prompt (Windows):**
    ```bash
    python3 crime_analyzer.py
    ```
    *The script assumes the CSV file has columns named 'Primary Type', 'Community Area', and 'Date'. If your data uses different column names, you will need to adjust the column names used in the Python script accordingly.*

## Areas for Potential Expansion

*   **Data Visualization:**  The script currently outputs text-based results. Integrating data visualization libraries could enhance the presentation of findings through charts and graphs.
*   **More Sophisticated Analysis:**  The script performs basic descriptive analysis.  Expanding to include more advanced statistical techniques, such as correlation analysis, regression modeling (to identify factors influencing crime rates), or time series forecasting, would provide deeper insights.
*   **Interactive User Interface:**  Developing a web-based or desktop application with a user interface would make the analysis more accessible and user-friendly for non-technical users, allowing them to explore the data and generate reports easily.
*   **Error Handling and Data Validation:**  In a production environment, more robust error handling and data validation would be essential to ensure the script can handle missing data, unexpected data formats, and other real-world data quality issues gracefully.

## Author

Darrell Sanders
https://www.linkedin.com/in/dcs11/
---
*This README.md file was created to explain the `crime_analyzer.py` code sample for a job application.*