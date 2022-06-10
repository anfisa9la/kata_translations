import unittest


def multiply(arr):
    return int(arr[0]) * int(arr[1])


class TestMultiply(unittest.TestCase):

    def test_1(self):
        self.assertEqual(0, multiply(['0', '2']))
        self.assertEqual(0, multiply(['100', '0']))
        self.assertEqual(0, multiply(['0', '0']))

    def test_2(self):
        self.assertEqual(-10, multiply(['-1', '10']))
        self.assertEqual(-17, multiply(['-17', '1']))
        self.assertEqual(64, multiply(['-8', '-8']))
        self.assertEqual(-80, multiply(['-20', '4']))

    def test_3(self):
        self.assertEqual(70, multiply(['7', '10']))
        self.assertEqual(81, multiply(['9', '9']))
        self.assertEqual(28, multiply(['7', '4']))
        self.assertEqual(180, multiply(['20', '9']))

    def test_4(self):
        self.assertEqual(70, multiply(['7', '10']))
        self.assertEqual(81, multiply(['9', '9']))
        self.assertEqual(28, multiply(['7', '4']))
        self.assertEqual(180, multiply(['20', '9']))
