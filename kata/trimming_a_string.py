import unittest


def trim(string, size):
    return string if len(string) <= size else string[0:size] + '...' if size <= 3 else string[0:size-3] + '...'


class TestMyDef(unittest.TestCase):

    def test_8(self):
        self.assertEqual(trim("He", 1), "H...")

    def test_9(self):
        self.assertEqual(trim("Hey", 2), "He...")

    def test_10(self):
        self.assertEqual(trim("Creating kata is fun", 4), "C...")

    def test_11(self):
        self.assertEqual(trim("Coding rocks", 12), "Coding rocks")

    def test_12(self):
        self.assertEqual(trim("Code Wars is pretty rad", 50), "Code Wars is pretty rad")

    def test_13(self):
        self.assertEqual(trim("London is freezing", 18), "London is freezing")
