sum = 0
value = 2000000
checked = [false]*value
count = 2

while count < value
    if checked[count] == false
        sum += count
        (count...value).step(count).each do |i|
            checked[i] = true
        end
    end
    count = count + 1
end

puts sum