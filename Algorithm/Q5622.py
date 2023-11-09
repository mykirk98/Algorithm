dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

A = input()
sum = 0
for i in A:
    for j in dial:
        if i in j:
            B = dial.index(j) + 3
            sum += B

print(sum)