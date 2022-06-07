import unittest


def spongebob_meme(s):
    return "".join(a + b for (a, b) in zip(s.upper()[::2], (s + ' ').lower()[1::2]))[:len(s)]


class SpongebobMemeTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual('TeSt', spongebob_meme('test'))

    def test_2(self):
        self.assertEqual('StOp mAkInG SpOnGeBoB MeMeS!', spongebob_meme('stop Making spongebob Memes!'))

    def test_3(self):
        self.assertEqual('QwErTyUiOpAsDfGhJkL', spongebob_meme('qwertyuiopasdfghjkl'))

    def test_4(self):
        self.assertEqual('QwErTyUiOpAsDfGhJkL', spongebob_meme('QWERTYUIOPASDFGHJKL'))
