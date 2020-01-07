import unittest

from src.lib.numeral_system import *


class TestNumeralSystem(unittest.TestCase):
    tests = [
        {'dec_num': 4, 'base': 2, 'base_num': '100'},
        {'dec_num': 25, 'base': 2, 'base_num': '11001'},
        {'dec_num': 45678, 'base': 2, 'base_num': '1011001001101110'},
        {'dec_num': 5, 'base': 3, 'base_num': '12'},
        {'dec_num': 56, 'base': 3, 'base_num': '2002'},
        {'dec_num': 19684, 'base': 3, 'base_num': '1000000001'},
        {'dec_num': 11, 'base': 4, 'base_num': '23'},
        {'dec_num': 52, 'base': 4, 'base_num': '310'},
        {'dec_num': 2852, 'base': 4, 'base_num': '230210'},
        {'dec_num': 9, 'base': 5, 'base_num': '14'},
        {'dec_num': 65, 'base': 5, 'base_num': '230'},
        {'dec_num': 32178, 'base': 5, 'base_num': '2012203'},
        {'dec_num': 7, 'base': 6, 'base_num': '11'},
        {'dec_num': 27, 'base': 6, 'base_num': '43'},
        {'dec_num': 19683, 'base': 6, 'base_num': '231043'},
        {'dec_num': 12, 'base': 7, 'base_num': '15'},
        {'dec_num': 90, 'base': 7, 'base_num': '156'},
        {'dec_num': 31795, 'base': 7, 'base_num': '161461'},

        {'dec_num': 56, 'base': 16, 'base_num': '38'},
        {'dec_num': 489, 'base': 16, 'base_num': '1e9'},
        {'dec_num': 149325, 'base': 16, 'base_num': '2474d'},

        {'dec_num': 65, 'base': 31, 'base_num': '23'},
        {'dec_num': 250, 'base': 31, 'base_num': '82'},
        {'dec_num': 854123, 'base': 31, 'base_num': 'skob'},
    ]

    def test_dec_to_base(self):
        for test in self.tests:
            self.assertEqual(test['base_num'], dec_to_base(test['dec_num'], test['base']))

    def test_base_to_dec(self):
        for test in self.tests:
            self.assertEqual(test['dec_num'], base_to_dec(test['base_num'], test['base']))

    def test_encode_success(self):
        self.assertEqual('0', encode(0))
        self.assertEqual('5', encode(5))
        self.assertEqual('a', encode(10))
        self.assertEqual('h', encode(17))
        self.assertEqual('z', encode(35))

    def test_encode_exception(self):
        with self.assertRaises(AlphabetError) as cm:
            encode(36)
        err = cm.exception
        self.assertEqual(str(err), 'There is no index 36 in the alphabet.')

    def test_decode_success(self):
        self.assertEqual(3, decode('3'))
        self.assertEqual(8, decode('8'))
        self.assertEqual(16, decode('g'))
        self.assertEqual(24, decode('o'))
        self.assertEqual(34, decode('y'))

    def test_decode_exception(self):
        with self.assertRaises(AlphabetError) as cm:
            decode('$')
        err = cm.exception
        self.assertEqual(str(err), 'There is no symbol $ in the alphabet.')


if __name__ == '__main__':
    unittest.main()
