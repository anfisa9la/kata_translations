import unittest


# solution
def power(num, p):
    return num ** p


# preloaded code
def greet(num, p):
    pass


class TestPower(unittest.TestCase):

    def test_1(self):
        self.assertEqual(power(2, 2), 4)
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, 4), 16)
        self.assertEqual(power(2, 5), 32)

    def test_2(self):
        self.assertEqual(power(2, 5), 2 ** 5)
        self.assertEqual(power(3, 50), 3 ** 50)
        self.assertEqual(power(2, 200), 2 ** 200)
        self.assertEqual(power(200, 0), 1)

    def test_3(self):
        self.assertEqual(power(2, -5), 2 ** -5)
        self.assertEqual(power(-3, 5), (-3) ** 5)
        self.assertEqual(power(2, -200), 2 ** -200)
        self.assertEqual(power(-200, 0), 1)
