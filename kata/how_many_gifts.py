import unittest


# solution
def how_many_gifts(max_budget, gifts):
    if min(gifts) > max_budget:
        return 0
    else:
        gifts.sort()
        while sum(gifts) > max_budget:
            sum(gifts) - gifts[-1]
            gifts.pop(-1)
        return len(gifts)


class HowManyGiftsTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(4, how_many_gifts(20, [13, 2, 4, 6, 1]))

    def test_2(self):
        self.assertEqual(8, how_many_gifts(90, [87, 3, 5, 25, 1, 3, 4, 6, 20]))

    def test_3(self):
        self.assertEqual(9, how_many_gifts(100, [6, 94, 10, 45, 2, 4, 5, 6, 8, 1]))

    def test_4(self):
        self.assertEqual(0, how_many_gifts(0, [1]))

    def test_5(self):
        self.assertEqual(7, how_many_gifts(910238, [1231, 42340232403, 9324810, 23948, 19823, 1, 3209, 23894, 1093]))

    def test_6(self):
        self.assertEqual(217, how_many_gifts(918,
                                             [1, 1, 1, 900, 1, 56, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                              1, 1, 1, 1, 1, 1, 1,
                                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2,
                                              2, 2, 2, 2, 2, 3, 3,
                                              3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6,
                                              6, 6, 6, 6, 7, 7, 7,
                                              7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0,
                                              0, 0, 0, 0, 1, 1, 1,
                                              1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0,
                                              0, 0, 0, 0, 4, 4, 4,
                                              4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7,
                                              7, 7, 7, 7, 7, 7, 8,
                                              8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
                                              0, 0]))

    def test_7(self):
        self.assertEqual(110,
                         how_many_gifts(10000000, [4, 4, 4, 189189956, 489498, 489489, 6456321, 564156, 231231, 123,
                                                   4674, 74987, 45646, 1411, 5496, 9474, 42, 1111, 1, 1, 1, 0, 0, 0, 0,
                                                   0, 0, 0, 0, 4, 4, 4, 478789, 454, 31321, 2222, 33334, 45465, 489479,
                                                   989, 4546, 123, 321, 456, 987, 453, 741, 1231, 45468, 1, 0, 0, 0, 0,
                                                   0, 0, 0, 0, 0, 0, 0, 123, 1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 1,
                                                   646, 798798, 22, 45, 7897, 45132, 666, 1132, 12, 5478, 42, 42, 42,
                                                   42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42,
                                                   42, 42, 42, 42, 42, 42]))

    def test_8(self):
        self.assertEqual(12, how_many_gifts(90, [10, 10, 10, 10, 10, 10, 5, 5, 5, 5, 5, 5]))

    def test_9(self):
        self.assertEqual(4, how_many_gifts(4, [1, 1, 1, 1]))

    def test_10(self):
        self.assertEqual(56, how_many_gifts(1,
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                             0,
                                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                             0,
                                             0, 0, 0, 0]))

    def test_11(self):
        self.assertEqual(0, how_many_gifts(10, [15, 17, 20]))

    def test_12(self):
        self.assertEqual(1, how_many_gifts(10, [10, 11]))

    def test_13(self):
        self.assertEqual(0, how_many_gifts(10, [15, 17, 20]))

    def test_14(self):
        self.assertEqual(4, how_many_gifts(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
