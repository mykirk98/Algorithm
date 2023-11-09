N = int(input())

lets_start = N
counter = 0

while True:
    A, B = lets_start // 10, lets_start % 10

    sum = A + B

    first_digit = sum % 10

    next_number = B * 10 + first_digit

    lets_start = next_number
    counter += 1
    if N == next_number:
        break

print(counter)