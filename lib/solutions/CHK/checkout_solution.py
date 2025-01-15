# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    prices = {
        "A": 50,
        "B": 30,
        "C": 25,
        "D": 15
    }

    purchases = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }

    for char in skus:
        if char not in prices:
            raise Exception("Invalid SKU")
        


