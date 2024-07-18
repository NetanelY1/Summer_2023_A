def sum_of_digit(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum

for i in range(1, 1000):
    if i % sum_of_digit(i) == 0:
        print(i)
    