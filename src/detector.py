import pandas as pd
import sqlite3
import os

def analyze_vulnerability():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, 'data', 'sentinel.db')
    
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()

    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # 🚨 Pattern 1: Gambling Spiral (More than 5 hits in 7 days)
    gambling = df[df['category'] == 'Gambling']
    spiral_users = gambling.groupby('user_id').filter(lambda x: len(x) >= 5)['user_id'].unique().tolist()

    # 🚨 Pattern 2: Financial Resilience (High relative spend)
    avg_spend = df.groupby('user_id')['amount'].transform('mean')
    shock_users = df[df['amount'] > (avg_spend * 3)]['user_id'].unique().tolist()

    return spiral_users, shock_users