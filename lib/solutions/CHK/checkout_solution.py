# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus: str) -> int:
    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }

    purchases = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }

    total = 0

    for char in skus:
        if char not in prices:
            raise Exception("Invalid SKU")
        
        purchases[char] += 1
        
        if purchases["A"] % 3 == 0 and purchases["A"] != 0:
            total += 30
            continue

        if purchases["B"] % 2 == 0 and purchases["B"] != 0:
            total += 15
            continue

        total += prices[char]
    
    return total


