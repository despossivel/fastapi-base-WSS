import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
DB = os.getenv('DB')
  
def query_orders(customer_name, start_date, end_date):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute('''
    SELECT SUM(order_value) AS total_order_value
    FROM orders
    WHERE customer_name = ? AND order_date BETWEEN ? AND ?
    ''', (customer_name, start_date, end_date))

    result = cursor.fetchone()
    total_order_value = result[0] if result else 0

    conn.close()
    return total_order_value
