import random

def get_numbers_ticket(min, max, quantity):
    
    try:
        min = int(min)
        max = int(max)
        quantity = int(quantity)
    except Exception as e:
        print(e)
        return []

    if min < 1 or max > 1000 or quantity > max - min + 1:
        return []

    min_max_range = [number for number in range(min, max + 1)]
    random_sequence = random.sample(min_max_range, quantity)
    random_sequence.sort()

    return random_sequence
    
    

print(get_numbers_ticket(100, 200, 10))
print(get_numbers_ticket(1, 10, 11))
print(get_numbers_ticket(10, 1, 11))
print(get_numbers_ticket(10, 10, 10))
print(get_numbers_ticket(1, 10, 0))
        