from collections import Counter

num_of_primes = {}

def get_prime_factors(num_to_factor):
    '''Finds all the prime factors of the num to factor'''
    toReturn = []
    count = 2
    left_to_factor = num_to_factor
    while left_to_factor > 1:
        while left_to_factor % count == 0:
            toReturn.append(count)
            left_to_factor = int(left_to_factor/count)
        count = count + 1
                
    return toReturn
    
def get_lcm_of_all_below(num):
    global num_of_primes
    '''Finds lowest common multiple of all the integers from 1 to num'''
    for i in range(2, num + 1):
        factors = get_prime_factors(i)
        fact_count = Counter(factors)
        for j in fact_count:
            if num_of_primes.has_key(j):
                num_of_primes[j] = max(num_of_primes[j], fact_count[j])
            else:
                num_of_primes[j] = fact_count[j]
    print num_of_primes
    result = 1
    for i in num_of_primes:
        result = result * int(i)**num_of_primes[i]
    return result
    
high_bound = raw_input('Enter the number that you want to be the highest bound of the numbers that you want to find the lcm of:')

print get_lcm_of_all_below(int(high_bound))