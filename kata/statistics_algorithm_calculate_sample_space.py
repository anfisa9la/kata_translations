import unittest

coin = ['heads', 'tails']
dice = [1, 2, 3, 4, 5, 6]


def all_possible_outcomes_of_multiple_trials(var, trials):
    return var.len ** trials


class TestMyAlgorithm(unittest.TestCase):

    def test_1(self):
        self.assertEqual(all_possible_outcomes_of_multiple_trials(coin[1], 4))
