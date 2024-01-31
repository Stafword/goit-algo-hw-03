from datetime import datetime


def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        the_difference = today - input_date
        return the_difference.days
    except ValueError:
        print("Ви ввели невірні дані")


date_string = input("Веддіть дату РРРР-ММ-ДД: ")
print(get_days_from_today(date_string))
