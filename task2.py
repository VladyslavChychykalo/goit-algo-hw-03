import random


def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list[int]:
    if min_value < 1 or max_value > 1000 or min_value > max_value or quantity > (max_value - min_value + 1) or quantity < 1:
        return []

    numbers = random.sample(range(min_value, max_value + 1), quantity)

    return sorted(numbers)


lottery_numbers = get_numbers_ticket(1, 49, 6)

print("Ваші лотерейні числа:", lottery_numbers)
