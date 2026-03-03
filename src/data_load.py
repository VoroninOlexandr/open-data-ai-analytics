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

import os
if __name__ == "__main__":

    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    FILE_PATH = os.path.join(project_root, 'data', 'registerbeer.csv')


    df = load_local_data(FILE_PATH)