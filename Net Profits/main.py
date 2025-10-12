import pandas as pd
from sqlalchemy import create_engine


DATABASE_URL = "postgresql://postgres:inserthereyourpassword@localhost:5432/fastapi_clients_orders"

engine = create_engine(DATABASE_URL)

DATABASE_URL_two = "postgresql://postgres:inserthereyourpassword@localhost:5432/fastapi_company_purchases"

engine_two = create_engine(DATABASE_URL_two)

orders_df = pd.read_sql("""SELECT product_name, amount, price FROM orders""", engine)

purchases_df = pd.read_sql("""SELECT product_name, amount, price FROM purchases""", engine_two)

orders_df['revenue'] = orders_df['amount']*orders_df['price']

purchases_df['cost'] = purchases_df['amount']*purchases_df['price']

total_revenue = orders_df['revenue'].sum()

total_cost = purchases_df['cost'].sum()

net_profit = total_revenue - total_cost

print(net_profit)
print(total_cost)
print(total_revenue)
