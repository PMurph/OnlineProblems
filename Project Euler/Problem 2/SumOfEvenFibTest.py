from SumOfEvenFib import sum_of_even_fib as soef
import unittest as ut

class TestSumOfEvenFib(ut.TestCase):
    def test_of_sum_of_even_fib(self):
        self.assertEqual(soef(0), 0, 'Error: Input of 0 did not return 0')
        self.assertEqual(soef(2), 0, 'Error: Input of 2 did not return 0')
        self.assertEqual(soef(3), 2, 'Error: Input of 3 did not return 2')
        self.assertEqual(soef(4), 2, 'Error: Input of 4 did not return 2')
        self.assertEqual(soef(9), 10, 'Error: Input of 9 did not return 10')
        self.assertEqual(soef(55), 44, 'Error: Input of 55 did not return 44')
        self.assertEqual(soef(145), 188, 'Error: Input of 145 did not return 188')

if __name__ == '__main__':
    ut.main()