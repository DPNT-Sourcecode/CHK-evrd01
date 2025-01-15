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
        if char in purchases:
            purchases[char] += 1
        else:
            purchases[char] = 1

    for sku, count in purchases.items():
        total += calculate_total(sku, count, purchases)
    return total

def calculate_total(sku: int, count: int, purchases: dict) -> int:
        match sku:
            case "A":
                return calculate_A(count)
            case "B":
                return calculate_B(count)
            case "E":
                return calculate_E(count, purchases)
            case "F":
                return calculate_F(count)
            case "H":
                return calculate_H(count)
            case "K":
                return calculate_K(count)
            case "N":
                return calculate_N(count, purchases)
            case "P":
                return calculate_P(count)
            case "Q":
                return calculate_Q(count)
            case "R":
                return calculate_R(count, purchases)
            case "U":
                return calculate_U(count)
            case "V":
                return calculate_V(count)
            case _:
                return purchases[sku] * prices[sku]

def calculate_A(A_count):
    subtotal = 0
    fives = A_count // 5
    threes = (A_count % 5) // 3
    ones = (A_count % 5) % 3
    subtotal += prices["5A"] * fives
    subtotal += prices["3A"] * threes
    subtotal += prices["A"] * ones
    return subtotal

def calculate_B(B_count):
    subtotal = 0
    twos = B_count // 2
    ones = B_count % 2
    subtotal += prices["2B"] * twos
    subtotal += prices["B"] * ones
    return subtotal

def calculate_E(E_count, purchases):
    subtotal = 0
    subtotal += E_count * prices["E"]
    
    if "B" in purchases:
        existing_bs = purchases["B"]
    else:
        existing_bs = 0
    free_bs = E_count // 2

    if free_bs != 0:
        # I misunderstood - I thought that with the numbers the software wants for EEB - 2Es makes 80 and you get a free B.
        # You buy a 2nd, discounted B at 15 which makes 95, not 80. I was using the below line.
        # subtotal += prices["2B"] - (2 * prices["B"])
        # I initially assumed the new free Bs were not included in the input which added lots of confusion
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

def calculate_F(F_count: int) -> int:
    subtotal = 0
    discounts = F_count // 3
    subtotal += discounts * (2 * prices["F"])
    remaining = F_count % 3
    subtotal += remaining * prices["F"]
    return subtotal

def calculate_H(H_count: int) -> int:
    subtotal = 0
    tens = H_count // 10
    fives = (H_count % 10) // 5
    ones = (H_count % 10) % 5
    subtotal += prices["10H"] * tens
    subtotal += prices["5H"] * fives
    subtotal += prices["H"] * ones
    return subtotal

def calculate_K(K_count: int) -> int:
    subtotal = 0
    twos = K_count // 2
    ones = K_count % 2
    subtotal += prices["2K"] * twos
    subtotal += prices["K"] * ones
    return subtotal

def calculate_N(N_count: int, purchases: dict) -> int:
    subtotal = 0
    subtotal += N_count * prices["N"]

    if "M" in purchases:
        existing_ms = purchases["M"]
    else:
        existing_ms = 0

    free_ms = N_count // 3
    while existing_ms > 0 and free_ms > 0: 
        subtotal -= prices["M"]
        existing_ms -= 1
        free_ms -= 1
    return subtotal

def calculate_P(P_count: int) -> int:
    subtotal = 0
    fives = P_count // 5
    ones = P_count % 5
    subtotal += prices["5P"] * fives
    subtotal += prices["P"] * ones
    return subtotal

def calculate_Q(Q_count: int) -> int:
    subtotal = 0
    threes = Q_count // 3
    ones = Q_count % 3
    subtotal += prices["3Q"] * threes
    subtotal += prices["Q"] * ones
    return subtotal

def calculate_R(R_count: int, purchases) -> int:
    subtotal = 0
    subtotal += R_count * prices["R"]
    
    if "Q" in purchases:
        existing_qs = purchases["Q"]
    else:
        existing_qs = 0
    free_qs = R_count // 3

    if free_qs != 0:
        discounts_applied = 0
        while existing_qs > 0 and free_qs > 0:
            discounts_applied += 1
            if discounts_applied % 3 == 0 or (existing_qs - free_qs) % 3 != 0:
                subtotal -= prices["3Q"] - (2 *prices["Q"])
            elif discounts_applied % 3 != 0:
                subtotal -= prices["Q"]
            existing_qs -= 1
            free_qs -= 1
    print(subtotal)
    return subtotal

def calculate_U(U_count: int) -> int:
    subtotal = 0
    discounts = U_count // 4
    subtotal += discounts * (3 * prices["U"])
    remaining = U_count % 4
    subtotal += remaining * prices["U"]
    return subtotal

def calculate_V(V_count: int) -> int:
    subtotal = 0
    threes = V_count // 3
    twos = (V_count % 3) // 2
    ones = (V_count % 3) % 2
    subtotal += prices["3V"] * threes
    subtotal += prices["2V"] * twos
    subtotal += prices["V"] * ones
    return subtotal
