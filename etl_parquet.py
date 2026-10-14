
import pandas as pd
import os

print("[ETL] Building star schema Parquet tables...")

# 1. Read the original CSV files
df_cust = pd.read_csv("customers_raw.csv")
df_prod = pd.read_csv("products_raw.csv")
df_sales = pd.read_csv("sales_raw.csv")

# 2. Clean customer, product and sales data
df_cust = df_cust.drop_duplicates("customer_id").dropna()
df_prod = df_prod.drop_duplicates("product_id").dropna()
df_sales = df_sales.drop_duplicates("transaction_id").dropna()

# Keep only sales with positive quantities
df_sales = df_sales[df_sales["quantity"] > 0].copy()

# Convert transaction dates into actual dates
df_sales["transaction_date"] = pd.to_datetime(
    df_sales["transaction_date"]
)

# 3. Create the date dimension
dates = df_sales["transaction_date"].drop_duplicates().sort_values()

dim_date = pd.DataFrame({
    "date_id": dates.dt.strftime("%Y%m%d").astype("int64"),
    "full_date": dates.dt.strftime("%Y-%m-%d"),
    "day_of_week": dates.dt.day_name(),
    "month": dates.dt.month_name(),
    "quarter": "Q" + dates.dt.quarter.astype(str),
    "year": dates.dt.year.astype("int64"),
    "is_weekend": dates.dt.dayofweek.isin([5, 6])
})

# 4. Add date IDs to sales
df_sales["date_id"] = (
    df_sales["transaction_date"]
    .dt.strftime("%Y%m%d")
    .astype("int64")
)

# 5. Create the sales fact table
fact_sales = df_sales[
    [
        "transaction_id",
        "customer_id",
        "product_id",
        "date_id",
        "quantity",
        "unit_price",
        "total_amount"
    ]
].copy()

# 6. Prepare the four output folders
tables = ["dim_customer", "dim_product", "dim_date", "fact_sales"]

for table in tables:
    os.makedirs(f"curated/{table}", exist_ok=True)

# 7. Save each table as compressed Parquet
df_cust.to_parquet(
    "curated/dim_customer/dim_customer.parquet",
    engine="pyarrow", compression="snappy", index=False
)

df_prod.to_parquet(
    "curated/dim_product/dim_product.parquet",
    engine="pyarrow", compression="snappy", index=False
)

dim_date.to_parquet(
    "curated/dim_date/dim_date.parquet",
    engine="pyarrow", compression="snappy", index=False
)

fact_sales.to_parquet(
    "curated/fact_sales/fact_sales.parquet",
    engine="pyarrow", compression="snappy", index=False
)

print("[ETL] Done!")
print("Customer rows:", len(df_cust))
print("Product rows:", len(df_prod))
print("Date rows:", len(dim_date))
print("Sales rows:", len(fact_sales))
print("Output format: Parquet with Snappy compression")
