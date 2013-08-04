import math

def isPalindrome(num):
    num_str = str(num)
    digits = len(num_str)
    if digits == 1:
        return True
    else:
        return num_str[:int(math.floor(digits/2.0))] == num_str[-int(math.floor(digits/2.0)):][::-1]

max = 0

# assumes that the biggest palindromic number that is the product of two 3 digit numbers has both 3 digit numbers
# located between 900 and 999
for i in range(900, 999)[::-1]:
    for j in range(900, 999)[::-1]:
        if isPalindrome(i * j):
            if i*j > max:
                max = i*j

print "Max: ", max