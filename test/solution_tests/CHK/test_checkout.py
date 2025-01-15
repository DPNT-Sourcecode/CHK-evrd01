from solutions.CHK import checkout_solution

class TestCheckout:
    def test_checkout_illegal(self):
        items = "---"
        price = checkout_solution.checkout(items)
        assert price == -1

    def test_checkout_A(self):
        items = "A"
        price = checkout_solution.checkout(items)
        assert price == 50

    def test_checkout_B(self):
        items = "B"
        price = checkout_solution.checkout(items)
        assert price == 30

    def test_checkout_C(self):
        items = "C"
        price = checkout_solution.checkout(items)
        assert price == 20

    def test_checkout_D(self):
        items = "D"
        price = checkout_solution.checkout(items)
        assert price == 15

    def test_checkout_E(self):
        items = "E"
        price = checkout_solution.checkout(items)
        assert price == 40

    def test_checkout_all(self):
        items = "ABCD"
        price = checkout_solution.checkout(items)
        assert price == 115

    def test_checkout_A_discount(self):
        items = "AAAAA"
        price = checkout_solution.checkout(items)
        assert price == 200

    def test_checkout_B_discount(self):
        items = "BBB"
        price = checkout_solution.checkout(items)
        assert price == 75

    def test_checkout_AB_discount(self):
        items = "ABCDABABAA"
        price = checkout_solution.checkout(items)
        assert price == 340

    def test_checkout_AB_discount(self):
        items = "ABCDABCD"
        price = checkout_solution.checkout(items)
        assert price == 215

    def test_checkout_2E_B_discount_1(self):
        items = "BEE"
        price = checkout_solution.checkout(items)
        assert price == 80

    def test_checkout_2E_B_discount_2(self):
        items = "EEB"
        price = checkout_solution.checkout(items)
        assert price == 80

    def test_checkout_2E(self):
        items = "EE"
        price = checkout_solution.checkout(items)
        assert price == 80
    
    def test_checkout_EEEB(self):
        items = "EEEB"
        price = checkout_solution.checkout(items)
        assert price == 120