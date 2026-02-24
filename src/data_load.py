import pandas as pd


def load_local_data(file_path):

    try:
        df = pd.read_csv(file_path, sep=';')
        print("Дані успішно завантажено в пам'ять!")
        print(f"Розмір датасету: {df.shape[0]} рядків, {df.shape[1]} колонок.")
        return df
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return None


if __name__ == "__main__":
    FILE_PATH = "../data/registerbeer.csv"

    df = load_local_data(FILE_PATH)

    if df is not None:

        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', 15)
        pd.set_option('display.width', 1000)

        print(df.head(15))