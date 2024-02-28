"""
문제
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.
이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

출력
첫째 줄에 분수를 출력한다.
"""

def swap(a, b):
    tmp = a
    a = b
    b = tmp
    
    return a, b

X = int(input())
lineFlag = 1

while X > lineFlag:
    X -= lineFlag
    lineFlag += 1

a, b = 1, lineFlag

for x in range(X-1):
    a += 1
    b -= 1

if lineFlag % 2 == 1:
    a, b = swap(a, b)

print(f"{a}/{b}")