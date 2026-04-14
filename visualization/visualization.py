import os
import time
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Налаштування БД
DB_USER = os.getenv('DB_USER', 'admin')
DB_PASS = os.getenv('DB_PASS', 'secretpassword')
DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('DB_NAME', 'beer_db')

# Папка для збереження картинок (яку бачить web-контейнер)
PLOTS_DIR = '/app/plots'


def create_visualizations():
    print("⏳ Очікування даних для візуалізації...")
    time.sleep(15)

    try:
        # 1. ПІДКЛЮЧЕННЯ ДО БАЗИ (замість read_csv)
        engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}')
        df = pd.read_sql("SELECT * FROM beer_data", engine)

        os.makedirs(PLOTS_DIR, exist_ok=True)

        # 2. ВАША ЛОГІКА ОБРОБКИ ДАНИХ
        df['LICBEG'] = pd.to_datetime(df['LICBEG'], format='%d.%m.%Y', errors='coerce')
        df['month'] = df['LICBEG'].dt.month

        seasons = {
            'Зима': df['month'].isin([12, 1, 2]).sum(),
            'Весна': df['month'].isin([3, 4, 5]).sum(),
            'Літо': df['month'].isin([6, 7, 8]).sum(),
            'Осінь': df['month'].isin([9, 10, 11]).sum()
        }

        # 3. ПОБУДОВА ГРАФІКІВ (3 в 1)
        plt.figure(figsize=(15, 5))

        # Графік 1: Форми власності
        plt.subplot(1, 3, 1)
        tov_count = df['NM'].str.contains('ТОВАРИСТВО З ОБМЕЖЕНОЮ ВIДПОВIДАЛЬНIСТЮ', case=False, na=False).sum()
        pp_count = df['NM'].str.contains('ПРИВАТНЕ ПIДПРИЄМСТВО', case=False, na=False).sum()
        others = len(df) - tov_count - pp_count
        plt.pie([tov_count, pp_count, others], labels=['ТОВ', 'ПП', 'Інші'],
                autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#99ff99', '#ffcc99'])
        plt.title('1. Форми власності')

        # Графік 2: Розподіл по сезонах
        plt.subplot(1, 3, 2)
        plt.bar(seasons.keys(), seasons.values(), color=['#a2d2ff', '#ffd700', '#ffafcc', '#fb6f92'])
        plt.title('2. Розподіл по сезонах')
        plt.ylabel('Кількість ліцензій')

        # Графік 3: Актуальність ліцензій
        plt.subplot(1, 3, 3)
        df['LICEND'] = pd.to_datetime(df['LICEND'], format='%d.%m.%Y', errors='coerce')
        expired = (df['LICEND'] < pd.Timestamp.today()).sum()
        active = len(df) - expired
        plt.bar(['Прострочені', 'Активні'], [expired, active], color=['#ff4d4d', '#2ecc71'])
        plt.title('3. Актуальність ліцензій')

        plt.tight_layout()

        # 4. ЗБЕРЕЖЕННЯ В DOCKER VOLUME
        save_path = os.path.join(PLOTS_DIR, 'business_analysis.png')
        plt.savefig(save_path)
        plt.close()  # Важливо закривати замість plt.show()

        print(f"✅ Графік успішно збережено у: {save_path}")

    except Exception as e:
        print(f"❌ Помилка візуалізації: {e}")


if __name__ == "__main__":
    create_visualizations()