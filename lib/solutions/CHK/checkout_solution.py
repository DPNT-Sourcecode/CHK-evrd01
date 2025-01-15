# noinspection PyUnusedLocal
# skus = unicode string

prices = {
    "5A": 200,
    "3A": 130,
    "A": 50,
    "2B": 45,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10
}

def checkout(skus: str) -> int:

    purchases = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 10
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
        # elif key == "F":
            # total += calculate_F(number_bought)
        else:
            total += purchases[key] * prices[key]
    return total

def calculate_A(number_of_A: int) -> int:
    subtotal = 0
    fives = number_of_A // 5
    threes = (number_of_A % 5) // 3
    ones = (number_of_A % 5) % 3
    subtotal += prices["5A"] * fives
    subtotal += prices["3A"] * threes
    subtotal += prices["A"] * ones
    return subtotal

def calculate_B(number_of_B: int) -> int:
    subtotal = 0
    twos = number_of_B // 2
    ones = number_of_B % 2
    subtotal += prices["2B"] * twos
    subtotal += prices["B"] * ones
    return subtotal

def calculate_E(number_of_E: int, purchases: dict) -> int:
    subtotal = 0
    subtotal += number_of_E * prices["E"]
    
    existing_bs = purchases["B"]
    free_bs = number_of_E // 2
    if free_bs != 0:
        # I don't think I agree with the numbers the software wants for EEB - 2Es makes 80 and you get a free B.
        # You buy a 2nd, discounted B at 15 which makes 95, not 80
        # subtotal += prices["2B"] - (2 * prices["B"])
        # I misunderstood the input - I assumed the new free Bs were not included in the input which added lots of confusion
        discounts_applied = 0
        while existing_bs > 0 and free_bs > 0:
            discounts_applied += 1
            if discounts_applied %2 == 0 or (existing_bs - free_bs) % 2 != 0:
                subtotal -= prices["2B"] - prices["B"]
            elif discounts_applied % 2 != 0:
                subtotal -= prices["B"]
            existing_bs -= 1
            free_bs -= 1
    return subtotal

def calculate_F(number_of_F: int) -> int:
    subtotal = 0
    discounts = number_of_F // 3
    subtotal += discounts * (2 * prices["F"])
    remaining = number_of_F % 3
    subtotal += remaining * prices["F"]
    return subtotal
