from datetime import datetime

def get_days_from_today(date = None):

    if date is None:
        return None

    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except Exception as e:
        print(e)
        return None
        
    today = datetime.today().date()

    return (today - target_date).days
    
print(get_days_from_today("2026-04-27"))
print(get_days_from_today("2026-05-27"))
print(get_days_from_today("2025-05-27"))
print(get_days_from_today())
print(get_days_from_today(5))
print(get_days_from_today("25-05-27"))