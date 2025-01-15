
from solutions.CHK import checkout_solution

class TestCheckout:
    def test_checkout_1(self):
        items = "ABCD"
        checkout_solution.checkout(items)
        assert hello_solution.hello("John") == "Hello, John!"