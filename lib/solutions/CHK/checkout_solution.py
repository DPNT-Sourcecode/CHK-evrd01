# noinspection PyUnusedLocal
# skus = unicode string

prices = {
    "A": 50,
    "3A": 130,
    "5A": 200,
    "B": 30,
    "2B": 45,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "5H": 45,
    "10H": 80,
    "I": 35,
    "J": 60,
    "K": 80,
    "2K": 150,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "5P": 200,
    "Q": 30,
    "3Q": 80,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "2V": 90,
    "3V": 130,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50
}

def checkout(skus: str) -> int:
    purchases = {}
    total = 0

    for char in skus:
        if char not in prices:
            return -1
            # raise Exception("Invalid SKU")
        if char in purchases:
            purchases[char] += 1
        else:
            purchases[char] = 1

    for sku, count in purchases.items():
        if sku == "A":
            total += calculate_A(count)
        elif sku == "B":
            total += calculate_B(count)
        elif sku == "E":
            total += calculate_E(count, purchases)
        elif sku == "F":
            total += calculate_F(count)
        else:
            total += purchases[sku] * prices[sku]
    return total

def calcualte_total(sku: int, count: int, purchases: dict) -> int:
        match sku:
            case "A":
                return calculate_A(count)
            case "B":
                return calculate_B(count)
            case "E":
                return calculate_B(count)
            case "F":
                return calculate_B(count)
            case _:
                return purchases[sku] * prices[sku]

        # if sku == "A":
            # total += calculate_A(count)
        # elif sku == "B":
            # total += calculate_B(count)
        # elif sku == "E":
            # total += calculate_E(count, purchases)
        # elif sku == "F":
            # total += calculate_F(count)
        # else:
            # total += purchases[sku] * prices[sku]

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
    
    if "B" in purchases:
        existing_bs = purchases["B"]
    else:
        existing_bs = 0
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





