def sum_of_even_fib(max_num):
    sum = 0
    first = 1
    second = 2
    while second < max_num:
        if second % 2 == 0:
            sum = sum + second
        temp = first + second
        first = second
        second = temp
    return sum

input = input("Enter the max number you want to find the sum of even fibonacci numbers less than:")

sum = sum_of_even_fib(int(input))

print(sum)