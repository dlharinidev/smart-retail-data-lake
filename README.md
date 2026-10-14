# Smart Retail Data Lake using AWS

## Overview
A retail analytics data lake using Python, Amazon S3, Apache Parquet, AWS Glue Data Catalog, and Amazon Athena.

## Architecture
1. Generate sample retail CSV data using Python.
2. Transform CSV files into Parquet format.
3. Store raw and curated datasets in Amazon S3.
4. Register tables in the AWS Glue Data Catalog.
5. Analyze sales using Amazon Athena SQL queries.

## Technologies
- Python, Pandas, PyArrow
- Amazon S3
- AWS Glue Data Catalog
- Amazon Athena and SQL
- Apache Parquet

## Files
- generate_data.py: Generates sample datasets.
- etl_parquet.py: Converts CSV data into Parquet.
- customers_raw.csv: Sample customer data.
- products_raw.csv: Sample product data.
- sales_raw.csv: Sample sales data.

## Analysis
- Revenue by product category and membership tier
- Monthly revenue
- Top customers by revenue
- CSV versus Parquet query scan comparison

## Measured Result
Both comparison queries returned total revenue of 637330.01.
The CSV query scanned 8901 bytes, while the Parquet query scanned 1429 bytes, approximately 83.9% fewer bytes in this test.

## Run
Install the required Python packages, then run:
python generate_data.py
python etl_parquet.py

Generated Parquet files are excluded from Git because they can be recreated. AWS resources must be configured separately.
