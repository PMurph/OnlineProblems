import unittest as ut
import prime_gen as pg

class TestPrimeGen(ut.TestCase):
    def testGetPrime(self):
        self.assertEqual(pg.getPrime(1), 2)
        self.assertEqual(pg.getPrime(2), 3)
        self.assertEqual(pg.getPrime(4), 7)
        self.assertEqual(pg.getPrime(6), 13)
        self.assertEqual(pg.getPrime(10), 29)
        self.assertEqual(pg.getPrime(100), 541)
        
if __name__ == '__main__':
    ut.main()