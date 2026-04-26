from datetime import datetime

def get_days_from_today(date = None):
    try:
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        today = datetime.today().date()
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        print(target_date, today)
        return (today - target_date).days
    except Exception as e:
        print(e)
        return None
    