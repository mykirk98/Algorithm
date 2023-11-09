INPUT = input()

list = INPUT.split(',')
sum = 0

for l in list:
    sum += int(l)

print(sum)