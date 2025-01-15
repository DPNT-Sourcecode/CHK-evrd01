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

    def test_checkout_F(self):
        items = "F"
        price = checkout_solution.checkout(items)
        assert price == 10

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

    def test_checkout_BEBEEE(self):
        items = "BEBEEE"
        price = checkout_solution.checkout(items)
        assert price == 160

    def test_checkout_ABCDEABCDE(self):
        items = "ABCDEABCDE"
        price = checkout_solution.checkout(items)
        assert price == 280

    def test_checkout_6F(self):
        items = "FFFFFF"
        price = checkout_solution.checkout(items)
        assert price == 40
    
    def test_checkout_16H(self):
        items = "H" * 16
        price = checkout_solution.checkout(items)
        assert price == 135

    def test_checkout_5K(self):
        items = "K" * 5
        price = checkout_solution.checkout(items)
        assert price == 310

    def test_checkout_NNN(self):
        items = "NNN"
        price = checkout_solution.checkout(items)
        assert price == 120

    def test_checkout_NNNM(self):
        items = "NNNM"
        price = checkout_solution.checkout(items)
        assert price == 120

    def test_checkout_7P(self):
        items = "P" * 7
        price = checkout_solution.checkout(items)
        assert price == 300

    def test_checkout_8Q(self):
        items = "Q" * 8
        price = checkout_solution.checkout(items)
        assert price == 220

    def test_checkout_RRRRRQ(self):
        items = "RRRRRQ"
        price = checkout_solution.checkout(items)
        assert price == 250

    def test_checkout_3U(self):
        items = "U" * 3
        price = checkout_solution.checkout(items)
        assert price == 120

    def test_checkout_5U(self):
        items = "U" * 5
        price = checkout_solution.checkout(items)
        assert price == 160

    def test_checkout_6V(self):
        items = "V" * 6
        price = checkout_solution.checkout(items)
        assert price == 260

    def test_checkout_PPPPQRUVPQRUVPQRUVSU(self):
        items = "PPPPQRUVPQRUVPQRUVSU"
        price = checkout_solution.checkout(items)
        assert price == 730

    def test_checkout_QRUVQRUVQRUVSU(self):
        items = "QRUVQRUVQRUVSU"
        price = checkout_solution.checkout(items)
        assert price == 480

    def test_checkout_QRUVQRUVQRUVU(self):
        items = "QRUVQRUVQRUVU"
        price = checkout_solution.checkout(items)
        assert price == 460

    def test_checkout_QRQRQR(self):
        items = "QRQRQR"
        price = checkout_solution.checkout(items)
        assert price == 210

    def test_checkout_6N2M(self):
        items = "NNNNNNMM"
        price = checkout_solution.checkout(items)
        assert price == 240
    
    def test_checkout_group_purchase(self):
        items = "SXYSXY"
        price = checkout_solution.checkout(items)
        assert price == 90

    def test_checkout_group_purchase_long(self):
        items = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
        price = checkout_solution.checkout(items)
        assert price == 1602
