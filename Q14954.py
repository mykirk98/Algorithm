"""
문제
Consider the following function f defined for any natural number n:

f(n) is the number obtained by summing up the squares of the digits of n in decimal (or base-ten).

If n = 19, for example, then f(19) = 82 because 12 + 92 = 82.

Repeatedly applying this function f, some natural numbers eventually become 1. Such numbers are called happy numbers. For example, 19 is a happy number, because repeatedly applying function f to 19 results in:

f(19) = 12 + 92 = 82
f(82) = 82 + 22 = 68
f(68) = 62 + 82 = 100
f(100) = 12 + 02 + 02 = 1
However, not all natural numbers are happy. You could try 5 and you will see that 5 is not a happy number. If n is not a happy number, it has been proved by mathematicians that repeatedly applying function f to n reaches the following cycle:

4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4.

Write a program that decides if a given natural number n is a happy number or not.

입력
Your program is to read from standard input. The input consists of a single line that contains an integer, n (1 ≤ n ≤ 1,000,000,000)

출력
Your program is to write to standard output. Print exactly one line. If the given number n is a happy number, print out HAPPY; otherwise, print out UNHAPPY.
"""

N = int(input())

original = N

while N // 1 != 1:
    total = 0
    for n in str(N):
        total += int(n) ** 2
    
    N = total
    
    if N == 4:
        print('UNHAPPY')
        break

if N == 1:
    print('HAPPY')

#각 자릿수의 값을 제곱해서 더해주는 함수
# def h(a) :
#     s = 0
#     while a//1 != 0 :
#         s += (a%10)**2
#         a = int(a/10)
#     return (s)

# a = int(input())

# #각 자릿수의 제곱합이 1혹은 4가 될때 까지 반복해서 구해주는 반복문
# while True:
#     a = h(a)
#     if a == 4 :
#         print('UNHAPPY')
#         break
#     elif a == 1 :
#         print('HAPPY')
#         break