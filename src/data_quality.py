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


if __name__ == "__main__":
    check_quality("../data/registerbeer.csv")