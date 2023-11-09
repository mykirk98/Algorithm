N = map(int, input().split())

sum = 0

for n in N:
    sum += n ** 2

remain = sum % 10

print(remain)