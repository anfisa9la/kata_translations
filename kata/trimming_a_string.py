import unittest


def trim(string, size):
    return string if len(string) <= size else string[0:size] + '...' if size <= 3 else string[0:size-3] + '...'


class TestMyDef(unittest.TestCase):

    def test_1(self):
        self.assertEqual(trim("Creating kata is fun", 1), "C...")

    def test_2(self):
        self.assertEqual(trim("Creating kata is fun", 2), "Cr...")

    def test_3(self):
        self.assertEqual(trim("Creating kata is fun", 3), "Cre...")

    def test_4(self):
        self.assertEqual(trim("Creating kata is fun", 4), "Creat...")

    def test_5(self):
        self.assertEqual(trim("Creating kata is fun", 11), "Creating...")

    def test_6(self):
        self.assertEqual(trim("Creating kata is fun", 14), "Creating ka...")
