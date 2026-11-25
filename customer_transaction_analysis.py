
import pandas as pd

# 1. Load CSV files
transactions = pd.read_csv(
    "transactions.csv",
    parse_dates=["transaction_date"]
)

products = pd.read_csv("products.csv")

print("Transactions Data:")
print(transactions.head())

print("\nProducts Data:")
print(products.head())


# 2. Data Cleaning
transactions = transactions.dropna(
    subset=["quantity", "price"]
)

transactions = transactions[
    (transactions["quantity"] > 0) &
    (transactions["price"] > 0)
].copy()

# Normalize dates to group by calendar day
transactions["transaction_date"] = (
    transactions["transaction_date"].dt.normalize()
)


# 3. Calculate Total Amount
transactions["total_amount"] = (
    transactions["quantity"] * transactions["price"]
)


# 4. Daily Revenue
daily_revenue = (
    transactions.groupby("transaction_date")["total_amount"]
    .sum()
    .reset_index()
)

daily_revenue.columns = [
    "transaction_date",
    "daily_revenue"
]

daily_revenue = daily_revenue.sort_values(
    "transaction_date"
)

print("\nDaily Revenue:")
print(daily_revenue)


# 5. Top 5 Customers
top_customers = (
    transactions.groupby("customer_id")["total_amount"]
    .sum()
    .reset_index()
)

top_customers.columns = ["customer_id", "total_spent"]

top_customers = top_customers.sort_values(
    "total_spent",
    ascending=False
).head(5)

print("\nTop 5 Customers:")
print(top_customers)


# 6. Merge Transactions and Products
merged_data = pd.merge(
    transactions,
    products,
    on="product_id",
    how="left"
)


# 7. Category Summary
category_summary = (
    merged_data.groupby("category")
    .agg(
        total_quantity_sold=("quantity", "sum"),
        total_revenue=("total_amount", "sum"),
        average_unit_price=("price", "mean")
    )
    .reset_index()
)

category_summary = category_summary.sort_values(
    "total_revenue",
    ascending=False
)

print("\nCategory Summary:")
print(category_summary)


# 8. Monthly Brand Revenue Pivot
merged_data["month"] = (
    merged_data["transaction_date"].dt.to_period("M")
)

monthly_brand_pivot = pd.pivot_table(
    merged_data,
    values="total_amount",
    index="month",
    columns="brand",
    aggfunc="sum",
    fill_value=0
)

print("\nMonthly Brand Revenue:")
print(monthly_brand_pivot)


# 9. Export Results to CSV
daily_revenue.to_csv("daily_revenue.csv", index=False)

top_customers.to_csv("top_customers.csv", index=False)

category_summary.to_csv("category_summary.csv", index=False)

monthly_brand_pivot.to_csv("monthly_brand_pivot.csv")


print("\nAll analysis completed successfully!")
print("All output CSV files have been generated.")
