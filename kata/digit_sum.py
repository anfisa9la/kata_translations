import unittest


def digit_sum(string):
    return str((int(string) - 1) % 9 + 1) if int(string) != 0 else '0'


class TestDigitSum(unittest.TestCase):

    def test(self):
        self.assertEqual(digit_sum('1234'), '1')
        self.assertEqual(digit_sum('2468'), '2')
        self.assertEqual(digit_sum('1011'), '3')
        self.assertEqual(digit_sum('333'), '9')
        self.assertEqual(digit_sum('000'), '0')
        self.assertEqual(digit_sum('00000'), '0')
        self.assertEqual(digit_sum('0'), '0')
        self.assertEqual(digit_sum('1111111'), '7')
        self.assertEqual(digit_sum('11111111111'), '2')
