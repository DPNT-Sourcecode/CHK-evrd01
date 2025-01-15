from solutions.CHK import checkout_solution

class TestCheckout:
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
