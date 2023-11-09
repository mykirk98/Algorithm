A = int(input())
B = int(input())
C = int(input())

D = str(A * B * C)

counter = {'0' : 0,
        '1' : 0,
        '2' : 0,
        '3' : 0,
        '4' : 0,
        '5' : 0,
        '6' : 0,
        '7' : 0,
        '8' : 0,
        '9' : 0}

for d in D:
    counter[d] += 1

print(*counter.values(), sep='\n')      # * : 모든 bracket들 제거해주고 표시