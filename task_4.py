from datetime import datetime

date_format = "%Y.%m.%d"

# from_date додад для імітації різних дат відліку,
# наприклад, щоб перевірити чи попадають в список дні народження
# з наступного року

def get_upcoming_birthdays(users_list, from_date = None):

    if not isinstance(users_list, list):
        return None

    today_date = datetime.today().date()

    if from_date is not None:
        today_date = datetime.strptime(from_date, date_format).date()
    
    current_year = today_date.year

    bd_list = []

    for user in users_list:
        birth_date = datetime.strptime(user["birthday"], date_format).date()

        congrats_date = birth_date.replace(year = current_year)

        if congrats_date < today_date:
            congrats_date = congrats_date.replace(year = current_year + 1)

        days_left = (congrats_date - today_date).days
        
        if -1 < days_left < 8:
            
            if congrats_date.weekday() == 5:
                congrats_date = congrats_date.replace(day=congrats_date.day + 2)

            if congrats_date.weekday() == 6:
                congrats_date = congrats_date.replace(day=congrats_date.day + 1)

            bd_list.append({
                "name": user["name"],
                "congratulate_date": datetime.strftime(congrats_date, date_format)
            })    

    return bd_list

users = [
    {"name": "John Doe", "birthday": "1985.12.28"},
    {"name": "John Doe", "birthday": "1985.12.29"},
    {"name": "John Doe", "birthday": "1985.12.30"},
    {"name": "John Doe", "birthday": "1985.12.31"},
    {"name": "Jane Smith", "birthday": "1990.01.01"},
    {"name": "Jane Smith", "birthday": "1990.01.02"},
    {"name": "Jane Smith", "birthday": "1990.01.03"},
    {"name": "Jane Smith", "birthday": "1990.01.04"},
    {"name": "Jane Smith", "birthday": "1990.01.05"},
    {"name": "Jane Smith", "birthday": "1990.01.06"},
    {"name": "Jane Smith", "birthday": "1990.01.07"},
    {"name": "Jane ", "birthday": "1990.05.08"},
    {"name": " Smith", "birthday": "1990.04.08"},
    {"name": " Smith", "birthday": "1990.04.28"},
    {"name": " Smith", "birthday": "1990.05.04"}
]
res = get_upcoming_birthdays(users, "2024.12.27")
print(res)
