import random

def get_numbers_ticket(min, max, quantity):
    try:
        min = int(min)
        max = int(max)
        quantity = int(quantity)

        if min < 1 or max > 1000 or quantity > max - min + 1:
            return []

        min_max_range = [number for number in range(min, max + 1)]
        random_sequence = random.sample(min_max_range, quantity)
        random_sequence.sort()

        return random_sequence
    
    except Exception as e:
        print(e)
        return []

print(get_numbers_ticket(1, 2, 2))
        