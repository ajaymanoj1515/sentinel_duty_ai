import sqlite3
import random
import os
from datetime import datetime, timedelta

def create_mock_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')
    db_path = os.path.join(data_dir, 'sentinel.db')

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS transactions')
    c.execute('''CREATE TABLE transactions 
                 (id INTEGER PRIMARY KEY, user_id TEXT, amount REAL, category TEXT, timestamp TEXT)''')

    cats = ['Groceries', 'Rent', 'Gambling', 'Salary', 'Netflix', 'Transport', 'Loan Repayment']
    users = [f'UK_USER_{i:03}' for i in range(1, 11)] # 10 Mock Users
    
    for _ in range(200):
        u = random.choice(users)
        cat = random.choice(cats)
        amt = round(random.uniform(10, 800), 2)
        date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d %H:%M:%S')
        
        # Force a "Gambling Spiral" pattern for User 001
        if u == 'UK_USER_001' and random.random() > 0.5:
            cat, amt = 'Gambling', random.uniform(200, 500)
            
        c.execute("INSERT INTO transactions (user_id, amount, category, timestamp) VALUES (?,?,?,?)", (u, amt, cat, date))
    
    conn.commit()
    conn.close()
    print(f"✅ Database Ready: {db_path}")

if __name__ == "__main__":
    create_mock_data()