
import os
print(os.listdir(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT"))

import pandas as pd

df = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\data.csv", encoding='utf-8-sig')

print(df.head())

import os
print(os.getcwd())


import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\data.csv", encoding='utf-8-sig')

# Remove null customers
df = df.dropna(subset=['CustomerID'])

# Create total amount
df['total_amount'] = df['Quantity'] * df['UnitPrice']

# ---------------- CUSTOMERS ----------------
customers = df[['CustomerID','Country']].drop_duplicates()
customers.columns = ['customer_id','country']
customers.to_csv("customers.csv", index=False)

# ---------------- PRODUCTS ----------------
products = df[['StockCode','Description','UnitPrice']].drop_duplicates()
products.columns = ['product_id','product_name','price']
products.to_csv("products.csv", index=False)

# ---------------- ORDERS ----------------
orders = df.groupby(['InvoiceNo','CustomerID','InvoiceDate'])['total_amount'].sum().reset_index()
orders.columns = ['order_id','customer_id','order_date','order_amount']
orders.to_csv("orders.csv", index=False)

# ---------------- PAYMENTS ----------------
payments = orders[['order_id']].copy()
payments['payment_id'] = range(1, len(payments)+1)
payments['payment_method'] = np.random.choice(['UPI','Card','COD'], len(payments))
payments['payment_status'] = np.random.choice(['Success','Failed'], len(payments), p=[0.9,0.1])
payments.to_csv("payments.csv", index=False)

print("✅ 4 CSV files created successfully!")

import pandas as pd

import pandas as pd

customers = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\Customer 360 Segemtation\data\customers.csv")
orders = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\Customer 360 Segemtation\data\orders.csv")
products = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\Customer 360 Segemtation\data\products.csv")
payments = pd.read_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\Customer 360 Segemtation\data\payments.csv")



# REMOVE DUPLICATES
customers = customers.drop_duplicates()
orders = orders.drop_duplicates()
products = products.drop_duplicates()
payments = payments.drop_duplicates()

# REMOVE NULL VALUES
customers = customers.dropna()
orders = orders.dropna()
products = products.dropna()
payments = payments.dropna()

# FIX DATA TYPES
orders['order_date'] = pd.to_datetime(orders['order_date'])

# REMOVE NEGATIVE VALUES
orders = orders[orders['order_amount'] > 0]
products = products[products['price'] > 0]

customers.to_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\Customer 360 Segemtation\data\customers_clean.csv", index=False)
orders.to_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\Customer 360 Segemtation\data\orders_clean.csv", index=False)
products.to_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\Customer 360 Segemtation\data\products_clean.csv", index=False)
payments.to_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\Customer 360 Segemtation\data\payments_clean.csv", index=False)

print("✅ Cleaning Done")



customers = customers.sort_values(by='customer_id').reset_index(drop=True)

customers.to_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\Customer 360 Segemtation\data/customers_clean.csv", index=False)

customers = customers.drop_duplicates()
customers = customers.dropna()

# FIX THIS LINE 👇
customers['customer_id'] = customers['customer_id'].astype(int)

customers = customers.sort_values(by='customer_id').reset_index(drop=True)

customers.to_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\Customer 360 Segemtation\data/customers_clean.csv", index=False)


payments = orders[['order_id']].copy()

payments['payment_id'] = range(1, len(payments)+1)
payments['payment_method'] = np.random.choice(['UPI','Card','COD'], len(payments))
payments['payment_status'] = np.random.choice(['Success','Failed'], len(payments), p=[0.9,0.1])

# 🔥 IMPORTANT: correct column order
payments = payments[['payment_id','order_id','payment_method','payment_status']]

payments.to_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\Customer 360 Segemtation\data/payments_clean.csv", index=False)

orders = orders.drop_duplicates()
orders = orders.dropna()

# FIX DATA TYPES
orders['customer_id'] = orders['customer_id'].astype(int)
orders['order_date'] = pd.to_datetime(orders['order_date'])

# REMOVE NEGATIVE VALUES
orders = orders[orders['order_amount'] > 0]

orders.to_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\Customer 360 Segemtation\data/orders_clean.csv", index=False)

customers = customers.drop_duplicates(subset=['customer_id'])
customers.to_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\Customer 360 Segemtation\data/customers_clean.csv", index=False)

orders = orders.drop_duplicates(subset=['order_id'])

orders['customer_id'] = orders['customer_id'].astype(int)
orders['order_date'] = pd.to_datetime(orders['order_date'])

orders.to_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\Customer 360 Segemtation\data/orders_clean.csv", index=False)

products = products.drop_duplicates(subset=['product_id'])

products = products.dropna()

products['price'] = products['price'].astype(float)

products.to_csv(r"C:\Users\shiva\OneDrive\Desktop\python\PROJECT\Customer 360 Segemtation\data/products_clean.csv", index=False)