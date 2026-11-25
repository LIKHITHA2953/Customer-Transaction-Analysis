# Customer-Transaction-Analysis

# Customer Transaction Analysis with Pandas

## Project Overview

This project focuses on analyzing customer transactions
for ShopEase, an online retail company, using Python and Pandas.

The main objective is to clean transaction data, perform
data analysis, and generate useful business insights.

## Technologies Used

- Python
- Pandas
- CSV Files

## Dataset Files

1. transactions.csv - Contains customer purchase details.
2. products.csv - Contains product category and brand information.

## Tasks Performed

1. Loaded transaction and product CSV files using Pandas.
2. Converted transaction dates into datetime format.
3. Removed missing and invalid quantity and price values.
4. Calculated total amount for each transaction.
5. Analyzed daily revenue.
6. Identified the top 5 customers based on total spending.
7. Calculated sales performance for each product category.
8. Merged transaction and product datasets.
9. Created a monthly brand revenue pivot table.
10. Exported the analysis results into CSV files.

## Output Files

- daily_revenue.csv
- top_customers.csv
- category_summary.csv
- monthly_brand_pivot.csv

## How to Run the Project

### Step 1: Install dependencies

pip install -r requirements.txt

### Step 2: Run the Python script

python customer_transaction_analysis.py

## Conclusion

This project demonstrates the use of Pandas for data
cleaning, data manipulation, grouping, merging, and
reshaping to extract meaningful business insights.
