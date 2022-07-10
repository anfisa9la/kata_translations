# solution
def power(num, p):
    return num ** p


class TestMyFunc:

    def test_1(self):
        assert (power(2, 2), 4)
        assert (power(2, 3), 8)
        assert (power(2, 4), 16)
        assert (power(2, 5), 32)

    def test_2(self):
        assert (power(2, 5), 2 ** 5)
        assert (power(3, 50), 3 ** 50)
        assert (power(2, 200), 2 ** 200)
        assert (power(200, 0), 1)

    def test_3(self):
        assert (power(2, -5), 2 ** -5)
        assert (power(-3, 5), (-3) ** 5)
        assert (power(2, -200), 2 ** -200)
        assert (power(-200, 0), 1)
