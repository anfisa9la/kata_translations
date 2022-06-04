import unittest


def describe_age(age):
    return "You're a(n) " + ("kid" if age < 13 else "teenager" if age < 18 else "adult" if age < 65 else "elderly")


class DescribeAgeTest(unittest.TestCase):

    def test_kid(self):
        self.assertEqual("You're a(n) kid", describe_age(0))
        self.assertEqual("You're a(n) kid", describe_age(1))
        self.assertEqual("You're a(n) kid", describe_age(10))
        self.assertEqual("You're a(n) kid", describe_age(12))

    def test_teenager(self):
        self.assertEqual("You're a(n) teenager", describe_age(13))
        self.assertEqual("You're a(n) teenager", describe_age(15))
        self.assertEqual("You're a(n) teenager", describe_age(17))
        self.assertEqual("You're a(n) teenager", describe_age(14))

    def test_adult(self):
        self.assertEqual("You're a(n) adult", describe_age(18))
        self.assertEqual("You're a(n) adult", describe_age(22))
        self.assertEqual("You're a(n) adult", describe_age(40))
        self.assertEqual("You're a(n) adult", describe_age(51))
        self.assertEqual("You're a(n) adult", describe_age(60))
        self.assertEqual("You're a(n) adult", describe_age(64))

    def test_elderly(self):
        self.assertEqual("You're a(n) elderly", describe_age(65))
        self.assertEqual("You're a(n) elderly", describe_age(66))
        self.assertEqual("You're a(n) elderly", describe_age(79))
        self.assertEqual("You're a(n) elderly", describe_age(80))
        self.assertEqual("You're a(n) elderly", describe_age(110))