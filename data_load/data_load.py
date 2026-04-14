import os
import time
import pandas as pd
from sqlalchemy import create_engine


DB_USER = os.getenv('DB_USER', 'admin')
DB_PASS = os.getenv('DB_PASS', 'secretpassword')
DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('DB_NAME', 'beer_db')


CSV_PATH = '/app/data/registerbeer.csv'


def load_data():
    print("Очікування готовності бази даних...")
    time.sleep(5)

    try:

        print(f" Читання файлу {CSV_PATH}...")
        df = pd.read_csv(CSV_PATH, sep=';')


        print("Підключення до PostgreSQL...")
        engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}')


        df.to_sql('beer_data', engine, if_exists='replace', index=False)
        print(f"Успішно! {len(df)} рядків завантажено у БД (таблиця 'beer_data').")

    except FileNotFoundError:
        print(f"Помилка: Файл {CSV_PATH} не знайдено.")
    except Exception as e:
        print(f"Критична помилка: {e}")


if __name__ == "__main__":
    load_data()