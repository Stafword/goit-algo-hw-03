import random


def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= max - min + 1):
        print("Ви ввели некоректні вхідні дані. Перевірьте коректність даних")
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)


lottery_numbers = get_numbers_ticket(10, 14, 6)
print("Ваші лотерейні числа:", lottery_numbers)
