from datetime import datetime, timedelta


def get_upcoming_birthdays(users_list, from_date=None):
    
    if not isinstance(users_list, list):
        return None

    date_format = "%Y.%m.%d"
    
    if from_date:
        today_date = datetime.strptime(from_date, date_format).date()
    else:
        today_date = datetime.today().date()

    upcoming_birthdays = []

    for user in users_list:
        
        original_birthday = datetime.strptime(user["birthday"], date_format).date()
        birthday_this_year = original_birthday.replace(year=today_date.year)

        
        if birthday_this_year < today_date:
            birthday_this_year = birthday_this_year.replace(year=today_date.year + 1)

        days_until = (birthday_this_year - today_date).days
        
        if 0 <= days_until <= 7:
            congratulation_date = birthday_this_year
            
            
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime(date_format)
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.04.26"},
    {"name": "John Doe", "birthday": "1985.04.27"},
    {"name": "John Doe", "birthday": "1985.12.29"},
    {"name": "John Doe", "birthday": "1985.05.01"},
    {"name": "John Doe", "birthday": "1985.05.02"},
    {"name": "John Doe", "birthday": "1985.05.03"},
]
res = get_upcoming_birthdays(users)
print(res)
