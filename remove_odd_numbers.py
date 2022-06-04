import unittest


def remove_odd_numbers_from_array(a):
        for i in a:
            if i % 2 != 0:
                a.remove(i)
        print(a)
        return a


class TestRemoval(unittest.TestCase):

    def test_0(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [2, 4, 6, 8, 10]
        self.assertEqual(expected, remove_odd_numbers_from_array(input))

    def test_1(self):
        input = [2, 2, 5, 6, 7, 14, 8, 9, 7, 10, 12]
        expected = [2, 2, 6, 14, 8, 10, 12]
        self.assertEqual(expected, remove_odd_numbers_from_array(input))

    def test_2(self):
        input = [9, 178, 160, 86, 78, 1, 84, 99, 63, 163, 98, 783, 67, 83]
        expected = [178, 160, 86, 78, 84, 98]
        self.assertEqual(expected, remove_odd_numbers_from_array(input))

    def test_3(self):
        input = [19, 18, 16, 186, 7, 19, 814, 990, 3, 13, 8, 73, 71, 3]
        expected = [18, 16, 186, 814, 990, 8]
        self.assertEqual(expected, remove_odd_numbers_from_array(input))

    def test_4(self):
        input = [190, 180, 160, 1860, 70, 190, 8140, 9900, 30, 130, 80, 730, 710, 30]
        expected = [190, 180, 160, 1860, 70, 190, 8140, 9900, 30, 130, 80, 730, 710, 30]
        self.assertEqual(expected, remove_odd_numbers_from_array(input))

    def test_5(self):
        input = [10, 812, 1601, 1861, 71, 190, 803, 628, 8372, 81, 82, 9362, 7101, 301]
        expected = [10, 812, 190, 628, 8372, 82, 9362]
        self.assertEqual(expected, remove_odd_numbers_from_array(input))

    def test_6(self):
        input = []
        expected = []
        self.assertEqual(expected, remove_odd_numbers_from_array(input))

    def test_7(self):
        input = [1, 3, 5, 7, 9]
        expected = []
        self.assertEqual(expected, remove_odd_numbers_from_array(input))



#import codewars_test as test
#import solution # or from solution import example

# test.assert_equals(actual, expected, [optional] message)
# @test.describe("Example")
# def test_group():
   # @test.it("test case")
   # def test_case():
       # test.assert_equals(remove_odd_numbers_from_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [2, 4, 6, 8, 10])
       # test.assert_equals(remove_odd_numbers_from_array([2, 2, 5, 6, 7, 14, 8, 9, 7, 10, 12]), [2, 2, 6, 14, 8, 10, 12])
       # test.assert_equals(remove_odd_numbers_from_array([9, 178, 160, 86, 78, 1, 84, 99, 63, 163, 98, 783, 67, 83]), [178, 160, 86, 78, 84, 98])
       # test.assert_equals(remove_odd_numbers_from_array([19, 18, 16, 186, 7, 19, 814, 990, 3, 13, 8, 73, 71, 3]), [18, 16, 186, 814, 990, 8])
       # test.assert_equals(remove_odd_numbers_from_array([190, 180, 160, 1860, 70, 190, 8140, 9900, 30, 130, 80, 730, 710, 30]), [190, 180, 160, 1860, 70, 190, 8140, 9900, 30, 130, 80, 730, 710, 30])
       # test.assert_equals(remove_odd_numbers_from_array([]), [])
       # test.assert_equals(remove_odd_numbers_from_array([1, 3, 5, 7, 9]), [])
