import os
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

DB_USER = os.getenv('DB_USER', 'admin')
DB_PASS = os.getenv('DB_PASS', 'secretpassword')
DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('DB_NAME', 'beer_db')
PLOTS_DIR = '/app/plots'


def create_visualizations():
    print("⏳ Очікування даних...")
    time.sleep(15)
    try:
        engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}')
        df = pd.read_sql("SELECT * FROM beer_data", engine)

        os.makedirs(PLOTS_DIR, exist_ok=True)

        # Простий графік для гарантованого результату (пропуски)
        plt.figure(figsize=(8, 5))
        df.isnull().sum().plot(kind='bar', color='salmon')
        plt.title('Пропуски у даних')
        plt.tight_layout()
        plt.savefig(f"{PLOTS_DIR}/visual_report1.png")
        plt.close()

        # Графік типів даних
        plt.figure(figsize=(8, 5))
        df.dtypes.value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title('Типи даних')
        plt.tight_layout()
        plt.savefig(f"{PLOTS_DIR}/visual_report2.png")
        plt.close()

        print("Графіки збережено.")
    except Exception as e:
        print(f" Помилка візуалізації: {e}")


if __name__ == "__main__":
    create_visualizations()