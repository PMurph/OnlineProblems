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

input = input('Enter the number you want to find the largest prime factor of:')

the_max = max(get_prime_factors(int(input)))

print(the_max)