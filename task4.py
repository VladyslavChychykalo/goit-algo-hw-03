import datetime


def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    today = datetime.date.today()
    upcoming_birthdays = []

    for user in users:
        birth_date = datetime.datetime.strptime(
            user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birth_date.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 7:

            if birthday_this_year.weekday() >= 5:
                days_till_monday = 7 - birthday_this_year.weekday()
                congratulation_date = birthday_this_year + \
                    datetime.timedelta(days=days_till_monday)

            else:
                congratulation_date = birthday_this_year

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "2024.04.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
