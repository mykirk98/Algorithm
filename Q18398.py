"""
문제
In one of the beautiful cities of Afghanistan two sisters are going to program a simple game to help them solve their mathematics homework. Their homework asks them to calculate the sum and multiplication of two numbers. Your task is to help them to build a simple program for their homework.

입력
First line contains the number of test cases (T).

T test cases follow. For each test case, the first line represents the number of problems. Next N lines contains two integer numbers Ai, Bi.

출력
For every input expecting two integer numbers, first one represents the addition of two given numbers and second represents the multiplication separated by space.
"""

for T in range(int(input())):
    for N in range(int(input())):
        A, B = map(int, input().split())

        Sum = A + B
        Multiplication = A * B

        print(Sum, Multiplication)