# database.py
import sqlite3

def create_database():
    conn = sqlite3.connect('mydatabase.db')
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


def select_tasks():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, completed FROM tasks')
    tasks_from_db = [{'id': row[0], 'title': row[1], 'completed': bool(row[2])} for row in cursor.fetchall()]
    conn.close()
    return tasks_from_db


def create_task(title):
     # Save the task in the database
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (title, False))
    conn.commit()
    conn.close()



# def query_orders(customer_name, start_date, end_date):
#     conn = sqlite3.connect('mydatabase.db')
#     cursor = conn.cursor()

#     cursor.execute('''
#     SELECT SUM(order_value) AS total_order_value
#     FROM orders
#     WHERE customer_name = ? AND order_date BETWEEN ? AND ?
#     ''', (customer_name, start_date, end_date))

#     result = cursor.fetchone()
#     total_order_value = result[0] if result else 0

#     conn.close()
#     return total_order_value
