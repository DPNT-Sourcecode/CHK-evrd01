
from solutions.CHK import checkout_solution

class TestCheckout:
    def test_checkout_1(self):
        items = "ABCD"
        price = checkout_solution.checkout(items)
        assert price == 115
