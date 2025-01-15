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
        
        # if char == "A":
            # if purchases["A"] % 5 == 0 and purchases["A"] != 0:
                # continue
            # elif purchases["A"] % 3 == 0 and purchases["A"] != 0:
                # total += 30
                # continue

        # if char == "B" and purchases["B"] % 2 == 0 and purchases["B"] != 0:
            # total += 15
            # continue

        # if char == "E" and purchases["E"] % 2 == 0 and purchases["E"] != 0:
            # purchases["B"] += 1
            # if purchases["B"] %2 == 0:
                # total -= 15

        for key, value in dict.items():
            subtotal = 0
            if key == "A":
                total += calculate_A(value)
            if key == "B":
                total += calculate_B(value)
            if key == "E":
                total += calculate_E(value, purchases)
        # total += prices[char]
    
    return total

def calculate_A(value):
    subtotal = 0
    fives = value // 5
    threes = (value % 5) // 3
    ones = (value % 5) % 3
    subtotal += prices["5A"] * fives
    subtotal += prices["3A"] * threes
    subtotal += prices["A"] * ones
    return subtotal

def calculate_B(value):
    subtotal = 0
    twos = value // 2
    ones = value % 2
    subtotal += prices["2B"] * twos
    subtotal += prices["B"] * ones
    return subtotal

def calculate_E(value, purchases):
    subtotal = 0
    twos = value // 2
    already_purchased_b = purchases["B"]
    purchases["B"] += twos
    return subtotal
