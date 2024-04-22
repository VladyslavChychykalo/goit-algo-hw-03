import datetime


def get_days_from_today(date_str: str) -> int:
    try:
        input_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        today = datetime.date.today()
        difference = (today - input_date).days

        return difference
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")


print(get_days_from_today("2021-10-09"))
