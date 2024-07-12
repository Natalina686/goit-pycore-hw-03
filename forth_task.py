from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        current_year_birthday = birthday.replace(year=today.year)

        if current_year_birthday < today:
            current_year_birthday = current_year_birthday.replace(year=today.year + 1)

        days_until_birthday = (current_year_birthday - today).days

        if days_until_birthday <= 7:
            if current_year_birthday.weekday() >= 5:  # Якщо день народження у вихідний день
                days_until_birthday += (7 - current_year_birthday.weekday())  # Вітаємо наступного понеділка

            congratulation_date = current_year_birthday - timedelta(days=days_until_birthday)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays

# Приклад
users = [
    {"name": "Іванка", "birthday": "2006.05.15"},
    {"name": "Маланка", "birthday": "2000.10.11"}
]

print(get_upcoming_birthdays(users))
        