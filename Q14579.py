"""
문제
남규는 최근에 덧셈과 곱셈을 배웠다.

하지만 도현이는 남규가 제대로 배웠는지에 대해 의심을 가지고 있다.

그래서 도현이는 남규에게 문제를 내기로 했는데, 문제는 아래와 같다.

a, b (1 ≤ a < b ≤ 1000)가 주어졌을 때

(1+2+…+a) * (1+2+…+(a+1)) * … * (1+2+…+(b-1)) * (1+2+…+b)

의 값을 계산하라.

남규는 사실 이 값을 계산하지 못한다.

그래서 남규는 a, b가 주어졌을 때, 위의 값의 결과가 얼마인지 구하는 프로그램이 필요하다.

남규를 위해 위 식을 계산해내는 프로그램을 하나 만들어 주자.

입력
첫째 줄에 a, b (1 ≤ a < b ≤ 1000)가 주어진다.

출력
위의 문제의 결과를 출력한다.

단, 결과가 매우 커질 수 있으니 14579로 나눈 나머지를 출력한다.
"""

a, b = map(int, input().split())

result = 1
for i in range(a, b+1):
    result *= i * (i + 1) // 2

print(result % 14579)