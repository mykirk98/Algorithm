total = 0
for N in range(int(input())):
    width, height = map(int, input().split())
    
    if width == 136:
        total += 1000
    elif width == 142:
        total += 5000
    elif width == 148:
        total += 10000
    elif width == 154:
        total += 50000

print(total)