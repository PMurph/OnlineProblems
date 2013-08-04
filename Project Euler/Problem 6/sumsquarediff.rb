def diffSumSquares(num)
    sumnum = sumOfNums(num)
    return sumnum * sumnum - sumOfSquares(num)
end

def sumOfSquares(max_num)
    return max_num * (2 * max_num + 1) * (max_num + 1) / 6
end

def sumOfNums(max_num)
    return max_num * ( max_num + 1) / 2
end

puts "Enter the number you want to find the difference between the square of sum of the numbers and the sum of the squares of the numbers:"
input = Integer(gets.chomp)
puts diffSumSquares(input)