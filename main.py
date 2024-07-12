from datetime import datetime
def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        time_difference = current_date - input_date
        return time_difference.days
    except ValueError:
        return "Очикується інший формат дати - Рік-Місяць-День."
date = '2022-12-11'
print(get_days_from_today(date))