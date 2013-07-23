import math

def sum_of_prev(num):
    '''Returns the sum of the num + num-1 + ... + 2 + 1'''
    return math.floor(num*(num+1)/2)

def sum_multiples(max_num):
    '''Returns the sum of all the multiples of 3 and 5 less than max_num'''
    num_mult_three = math.floor((max_num-1) / 3)
    num_mult_five = math.floor((max_num-1) / 5)
    num_mult_three_and_five = math.floor((max_num-1) / 15)
    return sum_of_prev(num_mult_three) * 3 + sum_of_prev(num_mult_five) * 5 - sum_of_prev(num_mult_three_and_five) * 15
    
input = input("Enter the number you want to find the sum of all multiples of three and five below:")

answer = sum_multiples(int(input))

print(answer)