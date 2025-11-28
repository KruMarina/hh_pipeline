import sqlite3
import pandas as pd
import sys
from pathlib import Path

def view_database():
    try:
        if 'run_etl.py' in ' '.join(sys.argv):
            db_path = 'data/databases/hh_vacancies.db'  # Локальный путь
        else:
            # Для Airflow или прямого запуска
            db_path = '/tmp/airflow_data/databases/hh_vacancies.db'
        
        print(f"Поиск бд по пути: {db_path}")
        
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("SELECT * FROM vacancy_stats", conn)
        
        print("Данные из SQLite базы:")
        print(df)
        print(f"Всего записей: {len(df)}")
        
        conn.close()
        
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    view_database()