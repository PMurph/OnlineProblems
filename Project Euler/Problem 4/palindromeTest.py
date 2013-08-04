import unittest as ut
import palindrome as p

class PalindromeNumberTest(ut.TestCase):
    def testIsPalindromeNumber(self):
        self.assertTrue(p.isPalindrome(1), '1 is a palindrome number but isPalindrome(1) returned false.')
        self.assertFalse(p.isPalindrome(10), '10 is not a palindrome but isPalindrome(10) returned true.')
        self.assertTrue(p.isPalindrome(11), '11 is a palindrome but isPalindrome(11) returned false.')
        self.assertFalse(p.isPalindrome(12), '12 is a palindrome but isPalindrome(12) returned true.')
        self.assertTrue(p.isPalindrome(101), '101 is a palindrome but isPalindrome(101) returned false.')
        self.assertFalse(p.isPalindrome(201), '201 is a palindrome but isPalindrome(201) returned true.')
        self.assertTrue(p.isPalindrome(252), '252 is a palindrome but isPalindrome(252) returned false.')
        self.assertTrue(p.isPalindrome(1001), '1001 is a palindrome but isPalindrome(1001) returned false.')
        
        
if __name__ == '__main__':
    ut.main()