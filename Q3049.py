"""
문제
세 대각선이 한 점에서 만나지 않는 볼록 N각형이 주어졌을 때, 대각선의 교차점의 개수를 세는 프로그램을 작성하시오.

아래 그림은 위의 조건을 만족하는 한 육각형의 교차점 그림이다.



모든 내부각이 180도보다 작은 다각형을 볼록 다각형이라고 한다.

입력
첫째 줄에 N이 주어진다. (3 ≤ N ≤ 100)

출력
첫째 줄에 교차점의 개수를 출력한다.
"""

def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    return n * factorial(n-1)

def permutation(n, r):
    if r == 0:
        return 1
    
    r -= 1
    return n * permutation(n-1, r)

def combination(n, r):
    if n < r:
        return 0
    result = factorial(n) // (factorial(r) * factorial(n - r))

    return result

N = int(input())

print(combination(N, 4))