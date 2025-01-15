# noinspection PyUnusedLocal
# skus = unicode string

prices = {
    "5A": 200,
    "3A": 130,
    "A": 50,
    "2B": 15,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

def checkout(skus: str) -> int:

    purchases = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0
    }

    total = 0

    for char in skus:
        if char not in prices:
            return -1
            # raise Exception("Invalid SKU")
        purchases[char] += 1

    for key, number_bought in purchases.items():
        if key == "A":
            total += calculate_A(number_bought)
        elif key == "B":
            total += calculate_B(number_bought)
        elif key == "E":
            total += calculate_E(number_bought, purchases)
        else:
            total += purchases[key] * prices[key]
    return total

def calculate_A(number_of_A):
    subtotal = 0
    fives = number_of_A // 5
    threes = (number_of_A % 5) // 3
    ones = (number_of_A % 5) % 3
    subtotal += prices["5A"] * fives
    subtotal += prices["3A"] * threes
    subtotal += prices["A"] * ones
    return subtotal

def calculate_B(number_of_B):
    subtotal = 0
    twos = number_of_B // 2
    ones = number_of_B % 2
    subtotal += prices["2B"] * twos
    subtotal += prices["B"] * ones
    return subtotal

def calculate_E(number_of_E, purchases):
    subtotal = 0
    subtotal += number_of_E * prices["E"]

    twos = number_of_E // 2
    already_purchased_b = purchases["B"]
    purchases["B"] += twos
    discounts = 0
    if twos > 0:
        discounts = twos + (already_purchased_b % 2)
    subtotal -= (prices["2B"] - prices["B"]) * discounts
    return subtotal


