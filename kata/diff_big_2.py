import unittest


def diff_big_2(arr):
    return arr.pop((arr.index(max(arr)))) - max(arr)


class TestMyDef(unittest.TestCase):
    def test_1(self):
        self.assertEqual(diff_big_2([9, 99, 999]), 900, "Wrong answer!")

    def test_2(self):
        self.assertEqual(diff_big_2([10, 9, 4]), 1, "Wrong answer!")

    def codewars_tests(self):
        self.assertEqual(diff_big_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1, "Wrong answer!")
        self.assertEqual(diff_big_2([9, 99, 999]), 900, "Wrong answer!")
        self.assertEqual(diff_big_2([999, 99, 9]), 900, "Wrong answer!")
        self.assertEqual(diff_big_2([100, 100]), 0, "Wrong answer!")
        self.assertEqual(diff_big_2([1, 2, 10, 3, 4, 5, 6, 7, 8, 9]), 1, "Wrong answer!")
        self.assertEqual(diff_big_2([1, 2, 10, 3, 4, 5, 6, 7, 8, 9, 10]), 0, "Wrong answer!")
        self.assertEqual(diff_big_2(
            [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
             29, 30, 100]), 0, "Wrong answer!")
        self.assertEqual(diff_big_2(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), 1, "Wrong answer!")
        self.assertEqual(diff_big_2(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 100]), 50,
                         "Wrong answer!")
        self.assertEqual(diff_big_2(
            [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
             29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), 50,
                         "Wrong answer!")
        self.assertEqual(diff_big_2(
            [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
             29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 100]), 0,
                         "Wrong answer!")
        self.assertEqual(diff_big_2([100, 100, 100, 100, 100, 100, 100, 100, 100, 100]), 0, "Wrong answer!")
        self.assertEqual(diff_big_2([1, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]), 0, "Wrong answer!")
        self.assertEqual(diff_big_2([100, 100, 100]), 0, "Wrong answer!")
        self.assertEqual(diff_big_2([100, 100, 99]), 0, "Wrong answer!")
        self.assertEqual(diff_big_2([100, 99, 100]), 0, "Wrong answer!")
        self.assertEqual(diff_big_2([99, 100, 100]), 0, "Wrong answer!")
        self.assertEqual(diff_big_2([100, 99, 99]), 1, "Wrong answer!")
        self.assertEqual(diff_big_2([99, 100, 99]), 1, "Wrong answer!")
        self.assertEqual(diff_big_2([99, 100, 99]), 1, "Wrong answer!")
        self.assertEqual(diff_big_2([99, 99, 99]), 0, "Wrong answer!")
