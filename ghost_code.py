import unittest


def ghost_code(name):
    return f"Hello my name is {name}" if name else "Hello world!"

# test.assert_equals(ghost_code("Anfisa"), "Hello my name is Anfisa")
# test.assert_equals(ghost_code("Jared Leto"), "Hello my name is Jared Leto")
# test.assert_equals(ghost_code(""), "Hello world!", "Assertion Error for empty string")


class GhostCodeTests(unittest.TestCase):

    def test_valid_name(self):
        self.assertEqual(ghost_code("Anfisa"), "Hello my name is Anfisa")

    def test_valid_name_2(self):
        self.assertEqual(ghost_code("Jared Leto"), "Hello my name is Jared Leto")

    def test_empty_str(self):
        self.assertEqual(ghost_code(""), "Hello world!", "Assertion Error for empty string")


