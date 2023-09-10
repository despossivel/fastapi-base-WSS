# database.py
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
DB = os.getenv('DB')

def create_database():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        customer_name TEXT,
        order_date DATE,
        order_value FLOAT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT,
        completed BOOLEAN
    )
    ''') 

    conn.commit()
    conn.close()
