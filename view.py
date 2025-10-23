import sqlite3
import pandas as pd

def view_database():
    try:
        conn = sqlite3.connect('data/databases/hh_vacancies.db')
        
        df = pd.read_sql_query("SELECT * FROM vacancy_stats", conn)
        
        print("Данные из SQLite базы:")
        print(df)
        
        print(f"Всего записей: {len(df)}")
        
        conn.close()
        
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    view_database()