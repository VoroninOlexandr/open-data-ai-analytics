import pandas as pd
import matplotlib.pyplot as plt
import os


def create_visualizations(file_path):
    if not os.path.exists(file_path):
        return

    df = pd.read_csv(file_path, sep=';')

    df['LICBEG'] = pd.to_datetime(df['LICBEG'], format='%d.%m.%Y', errors='coerce')
    df['month'] = df['LICBEG'].dt.month

    seasons = {
        'Зима': df['month'].isin([12, 1, 2]).sum(),
        'Весна': df['month'].isin([3, 4, 5]).sum(),
        'Літо': df['month'].isin([6, 7, 8]).sum(),
        'Осінь': df['month'].isin([9, 10, 11]).sum()
    }

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    tov_count = df['NM'].str.contains('ТОВАРИСТВО З ОБМЕЖЕНОЮ ВIДПОВIДАЛЬНIСТЮ', case=False, na=False).sum()
    pp_count = df['NM'].str.contains('ПРИВАТНЕ ПIДПРИЄМСТВО', case=False, na=False).sum()
    others = len(df) - tov_count - pp_count
    plt.pie([tov_count, pp_count, others], labels=['ТОВ', 'ПП', 'Інші'],
            autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#99ff99', '#ffcc99'])
    plt.title('1. Форми власності')

    plt.subplot(1, 3, 2)
    plt.bar(seasons.keys(), seasons.values(), color=['#a2d2ff', '#ffd700', '#ffafcc', '#fb6f92'])
    plt.title('2. Розподіл по сезонах')
    plt.ylabel('Кількість ліцензій')

    plt.subplot(1, 3, 3)
    df['LICEND'] = pd.to_datetime(df['LICEND'], format='%d.%m.%Y', errors='coerce')
    expired = (df['LICEND'] < pd.Timestamp.today()).sum()
    active = len(df) - expired
    plt.bar(['Прострочені', 'Активні'], [expired, active], color=['#ff4d4d', '#2ecc71'])
    plt.title('3. Актуальність ліцензій')

    plt.tight_layout()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    output_dir = os.path.join(project_root, 'data')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    save_path = os.path.join(output_dir, 'visual_report.png')
    plt.savefig(save_path)

    plt.show()


if __name__ == "__main__":
    csv_path = "../data/registerbeer.csv"
    create_visualizations(csv_path)