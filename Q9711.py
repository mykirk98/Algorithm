"""
문제
피보나치 수열은 아래와 같이 표현된다.

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

각 숫자는 앞의 두 숫자의 합으로 나타내는 것을 알 수 있다.

P와 Q 그리고 n이 주어질 때, P번째 피보나치 숫자를 Q로 나눈 나머지를 구하여라. 

입력
첫 번째 라인에는 정수 T개의 테스트 케이스가 주어진다.

각 테스트 케이스는 정수 P와 Q가 주어진다.

출력
각 테스트 케이스마다 "Case #x: M" 형식으로 출력한다.

x는 테스트 케이스 번호(1부터 시작), M은 P번째 피보나치 숫자를 Q로 나눈 나머지이다.
"""

fibonacci = [1, 1]

for i in range(10000):
    fibonacci.append(fibonacci[-2] + fibonacci[-1])

for i, T in enumerate(range(int(input()))):
    P, Q = map(int, input().split())
    print(f"Case #{i+1}:", fibonacci[P - 1] % Q)