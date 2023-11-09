A, B = map(int, input().split())
C = int(input())

if (A + ((B + C) // 60)) >= 24:
    A = (A + ((B + C) // 60)) - 24

else:
    A += (B + C) // 60

B = (B + C) % 60

print(f"{A} {B}")