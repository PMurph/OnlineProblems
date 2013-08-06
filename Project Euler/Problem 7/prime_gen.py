def getPrime(n):
    '''Returns the nth prime number'''
    count = 0
    i = 2
    num_list = [False] * n * 1000
    while count < n:
        if num_list[i] == False:
            count = count + 1
            for j in range(i, len(num_list), i):
                num_list[j] = True
        i = i + 1
    return i-1

if __name__ == "__main__":
    n = raw_input('Enter the number of the prime you want to get: ')
    print getPrime(int(n))