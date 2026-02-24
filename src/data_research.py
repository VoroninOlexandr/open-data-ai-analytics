import pandas as pd



def research_data(file_path):

    df = pd.read_csv(file_path, sep=';')

    df['LICBEG'] = pd.to_datetime(df['LICBEG'], format='%d.%m.%Y')
    df['LICEND'] = pd.to_datetime(df['LICEND'], format='%d.%m.%Y')

    print("\n[ГІПОТЕЗА 1]: Більшість броварень зареєстровані як ТОВ, а не ФОП чи ПП.")

    tov_count = df['NM'].str.contains('ТОВАРИСТВО З ОБМЕЖЕНОЮ ВIДПОВIДАЛЬНIСТЮ', case=False).sum()
    fop_count = df['NM'].str.contains('ФІЗИЧНА ОСОБА-ПІДПРИЄМЕЦЬ', case=False).sum()
    pp_count = df['NM'].str.contains('ПРИВАТНЕ ПIДПРИЄМСТВО', case=False).sum()
    total_companies = len(df)

    print(f"Всього записів: {total_companies}")
    print(f"- ТОВ: {tov_count} ({tov_count / total_companies * 100:.1f}%)")
    print(f"- ФОП: {fop_count} ({fop_count / total_companies * 100:.1f}%)")
    print(f"- ПП: {pp_count} ({pp_count / total_companies * 100:.1f}%)")

    print("\n[ГІПОТЕЗА 2]: Сезонність - найбільше ліцензій видається навесні (березень-травень).")

    df['start_month'] = df['LICBEG'].dt.month
    spring_count = df['start_month'].isin([3, 4, 5]).sum()
    total_valid_dates = df['start_month'].count()

    print(
        f"- Видано навесні (березень, квітень, травень): {spring_count} ({spring_count / total_valid_dates * 100:.1f}%)")

    print("\n[ГІПОТЕЗА 3]: Понад 15% виданих ліцензій вже прострочені.")

    today = pd.Timestamp.today()
    expired_count = (df['LICEND'] < today).sum()

    print(
        f"- Прострочених: {expired_count} із {total_companies} ({expired_count / total_companies * 100:.1f}%)")




if __name__ == "__main__":

    research_data("../data/registerbeer.csv")