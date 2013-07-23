import unittest as ut
import SumOfMultiples as som

class TestSumOfMultiples(ut.TestCase):
    def test_sum_multiples_valid(self):
        self.assertEqual(som.sum_multiples(0), 0, 'Error: Input of 0 did not return 0')
        self.assertEqual(som.sum_multiples(1), 0, 'Error: Input of 0 did not return 0')
        self.assertEqual(som.sum_multiples(3), 0, 'Error: Input of 3 did not return 0')
        self.assertEqual(som.sum_multiples(4), 3, 'Error: Input of 4 did not return 3')
        self.assertEqual(som.sum_multiples(5), 3, 'Error: Input of 5 did not return 3')
        self.assertEqual(som.sum_multiples(6), 8, 'Error: Input of 6 did not return 8')
        self.assertEqual(som.sum_multiples(7), 14, 'Error: Input of 7 did not return 14')
        self.assertEqual(som.sum_multiples(9), 14, 'Error: Input of 9 did not return 14')
        self.assertEqual(som.sum_multiples(10), 23, 'Error: Input of 10 did not return 23')
        self.assertEqual(som.sum_multiples(11), 33, 'Error: Input of 11 did not return 33')
        self.assertEqual(som.sum_multiples(16), 60, 'Error: Input of 16 did not return 60')
		
    def test_sum_of_prev_valid(self):
        self.assertEqual(som.sum_of_prev(0), 0, 'Error: Input of 0 did not return 0')
        self.assertEqual(som.sum_of_prev(1), 1, 'Error: Input of 1 did not return 1')
        self.assertEqual(som.sum_of_prev(2), 3, 'Error: Input or 2 did not return 3')
        self.assertEqual(som.sum_of_prev(6), 21, 'Error: Input of 6 did not return 21')

if __name__ == '__main__':
    ut.main()