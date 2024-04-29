"""
문제
청정수열은 길이가 
$2N$이고 
$1$부터 
$N$까지의 정수들이 정확히 두 번씩 등장하는 수열이다.

청정수열의 점수는 
$1$이상 
$N$이하인 모든 정수 
$i$에 대해 다음 값의 합이다.

(두 개의 
$i$ 사이에 있는 수의 합) × 
$i$ 
이때, "사이"는 양 끝의 
$i$를 포함한다.

길이가 
$2N$이면서 점수가 최소인 청정수열의 개수를 구해보자.

입력
첫째 줄에 정수 
$N$이 주어진다. (
$1 \le N \le 10$)

출력
첫째 줄에 길이가 
$2N$이면서 점수가 최소인 청정수열의 개수를 출력하라.
"""

# def factorial(n):
#     if n == 1:
#         return 1
    
#     return n * factorial(n-1)

# N = int(input())

# print(factorial(N))


N = int(input())

total = 1
for n in range(N, 0, -1):
    total *= n

print(total)