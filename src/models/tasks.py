# database.py
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
DB = os.getenv('DB')
  
def select_tasks():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, completed FROM tasks')
    tasks_from_db = [{'id': row[0], 'title': row[1], 'completed': bool(row[2])} for row in cursor.fetchall()]
    conn.close()
    return tasks_from_db
 
def create_task(title): 
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (title, False))
    conn.commit()
    conn.close()
 