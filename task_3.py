import re

def normalize_phone(phone_number = None):

    if phone_number is None:
        return ""
    
    try:
        phone_number = str(phone_number)
    except Exception as e:
        print(e)
        return ""
    
    only_digits_phone_number = re.sub(r"[^\d+]", "", phone_number)

    search = re.search(r"(\+)?(38)?(0\d{2})\d{7}", only_digits_phone_number)

    if search is None:
        return ""
    
    provider_phone_number = search.group()[-10:]

    return "+38" + provider_phone_number

print(normalize_phone({5}))
print(normalize_phone("     0503451234"))
print(normalize_phone("(050)8889900"))
print(normalize_phone("38050-111-22-22"))
print(normalize_phone("38050 111 23454 "))

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)