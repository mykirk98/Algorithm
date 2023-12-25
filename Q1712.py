"""
A : 고정 비용
B : 가변 비용
C : 판매 비용
"""

A, B, C = map(int, input().split())

if C <= B:
    print(-1)
else:
    print(int(A / (C - B) + 1))