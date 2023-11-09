"""방학 숙제"""
import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

korean, mathematics = math.ceil(A / C), math.ceil(B / D)

if korean > mathematics:
    print(L - korean)
else:
    print(L - mathematics)