import unittest as ut
from PrimeFactors import get_prime_factors as gpf

class PrimeFactorsTest(ut.TestCase):
    def testGetPrimeFactors(self):
        self.assertEqual(gpf(0), [], 'Error: Input of 0 did not return an empty list.')
        self.assertEqual(gpf(1), [], 'Error: Input of 1 did not return an empty list.')
        self.assertEqual(gpf(2), [2], 'Error: Input of 2 did not return an [2].')
        self.assertEqual(gpf(3), [3], 'Error: Input of 3 did not return [3].')
        self.assertEqual(gpf(4), [2, 2], 'Error: Input of 4 did not return [2, 2].')
        self.assertEqual(gpf(5), [5], 'Error: Input of 5 did not return [5].')
        self.assertEqual(gpf(6), [2, 3], 'Error: Input of 6 did not return [2, 3].')
        self.assertEqual(gpf(13195), [5, 7, 13, 29], 'Error: Input of 13195 did not return [5, 7, 13, 29].')

if __name__ == '__main__':
    ut.main()