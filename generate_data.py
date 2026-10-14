
import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

# 1. Generate customer data
customers = []
cities = ["Chennai", "Puducherry", "Bengaluru", "Hyderabad", "Coimbatore"]
tiers = ["Bronze", "Silver", "Gold", "Platinum"]

for i in range(1, 51):
    customers.append({
        "customer_id": f"C{i:03d}",
        "customer_name": f"Customer_{i}",
        "city": random.choice(cities),
        "membership_tier": random.choice(tiers),
        "signup_date": (
            datetime(2024, 1, 1) + timedelta(days=random.randint(0, 600))
        ).strftime("%Y-%m-%d")
    })

pd.DataFrame(customers).to_csv("customers_raw.csv", index=False)

# 2. Generate product data
products = []
categories = ["Electronics", "Groceries", "Clothing", "Home", "Books"]

for i in range(1, 21):
    products.append({
        "product_id": f"P{i:03d}",
        "product_name": f"Product_{i}",
        "category": random.choice(categories),
        "retail_price": round(random.uniform(50, 2000), 2),
        "stock_level": random.randint(0, 200)
    })

pd.DataFrame(products).to_csv("products_raw.csv", index=False)

# 3. Generate sales data
sales = []
start_date = datetime(2025, 1, 1)

for i in range(1, 201):
    quantity = random.randint(1, 5)
    unit_price = round(random.uniform(50, 2000), 2)

    sales.append({
        "transaction_id": f"T{i:04d}",
        "customer_id": f"C{random.randint(1, 50):03d}",
        "product_id": f"P{random.randint(1, 20):03d}",
        "quantity": quantity,
        "unit_price": unit_price,
        "total_amount": round(quantity * unit_price, 2),
        "transaction_date": (
            start_date + timedelta(days=random.randint(0, 364))
        ).strftime("%Y-%m-%d")
    })

pd.DataFrame(sales).to_csv("sales_raw.csv", index=False)

print("Retail CSV data generated successfully!")
print("Customers:", len(customers))
print("Products:", len(products))
print("Sales:", len(sales))

