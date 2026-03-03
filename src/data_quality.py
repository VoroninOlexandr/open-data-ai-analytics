import pandas as pd
import os


def check_quality(file_path):

    df = pd.read_csv(file_path, sep=';')

    print("\n1. Пропущені значення (NaN) у кожній колонці:")
    print(df.isnull().sum())

    print("\n2. Кількість повних дублікатів:")
    print(df.duplicated().sum())

    print("\n3. Типи даних колонок:")
    print(df.dtypes)


import os

if __name__ == "__main__":

    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)

    csv_path = os.path.join(project_root, 'data', 'registerbeer.csv')

    check_quality(csv_path)