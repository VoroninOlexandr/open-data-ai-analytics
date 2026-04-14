import os
import time
import pandas as pd
from sqlalchemy import create_engine

DB_USER = os.getenv('DB_USER', 'admin')
DB_PASS = os.getenv('DB_PASS', 'secretpassword')
DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('DB_NAME', 'beer_db')
REPORT_PATH = '/app/reports/research_report.txt'


def conduct_research():
    print("⏳ Очікування завантаження даних...")
    time.sleep(12)
    try:
        engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}')
        df = pd.read_sql("SELECT * FROM beer_data", engine)

        report_text = f"=== ЗВІТ ПРО ДОСЛІДЖЕННЯ ===\n\nСтатистика:\n{df.describe()}\n\nУнікальні:\n{df.nunique()}"

        os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
        with open(REPORT_PATH, 'w', encoding='utf-8') as f:
            f.write(report_text)
        print(" Звіт про дослідження збережено.")
    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    conduct_research()