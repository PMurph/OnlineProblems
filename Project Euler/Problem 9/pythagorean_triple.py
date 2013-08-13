import math

for i in range(1, 999):
    for j in range(1, 999):
        if int(math.sqrt(i * i + j * j) + i + j) == 1000 or i + j -int(math.sqrt(i * i + j * j)) == 1000:
            if math.sqrt(i*i + j*j) % 1.0 == 0:
                print i*j*int(math.sqrt(i*i+j*j))