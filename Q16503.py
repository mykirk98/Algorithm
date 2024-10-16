"""
문제
사칙연산에서 곱셈과 나눗셈은 덧셈과 뺄셈보다 먼저 계산한다. 덧셈과 뺄셈을 먼저 계산하고 싶을 때는 보통 가장 큰 연산 우선순위를 가지는 괄호를 사용하여 연산 순서를 지정한다. 예를 들어, 아래의 식은 연산 순서에 따라 두 가지 다른 결과가 나올 수 있다.

(2 + 3) × 4 = 20
2 + (3 × 4) = 14
연산 우선순위가 같은 곱셈과 나눗셈 또는 덧셈과 뺄셈만 있는 식에서는 보통 왼쪽에서 오른쪽 순서로 연산을 한다. 하지만 이런 상황에도 연산 순서에 따라 아래와 같이 두 가지 다른 결과가 나올 수 있다.

(6 ÷ 2) × 3 = 9
6 ÷ (2 × 3) = 1
만약 곱셈, 나눗셈, 덧셈, 뺄셈의 4가지 연산자의 연산 우선순위가 동등하다고 할 때, 괄호 없는 식에서 서로 다른 연산 순서의 계산 결과를 구하여라.

입력
첫 번째 줄에는 "K1 O1 K2 O2 K3" 형태로 식이 주어진다. 정수 Ki (1 ≤ Ki ≤ 1,000)는 피연산자를, 문자열 Oi는 곱셈(*), 나눗셈(/), 덧셈(+), 뺄셈(-) 중 한 가지 연산자를 의미한다.

나눗셈 연산은 정수 나눗셈으로 몫만 취하며, 피연산자 중 하나가 음수이면 양수로 바꿔 계산한 결괏값에 음수를 취한다. 또한, 계산 과정에서 0으로 나누어야 하는 식은 주어지지 않는다.

출력
주어진 식에서 서로 다른 연산 순서의 계산 결과가 작은 것을 첫 번째 줄에, 큰 것을 두 번째 줄에 출력한다.
"""

def calculation(a, b, operand):
    if operand == '+':
        result = a + b
    elif operand == '-':
        result = a - b
    elif operand == '*':
        result = a * b
    elif operand == '/':
        if a < 0 and b > 0:
            result = -(abs(a) // b)
        elif a > 0 and b < 0:
            result = -(a // abs(b))
        else:
            result = a // b
    
    return result

K1, O1, K2, O2, K3 = map(str, input().split())
K1, K2, K3 = int(K1), int(K2), int(K3)

result1 = calculation(a=K1, b=K2, operand=O1)
result1 = calculation(a=result1, b=K3, operand=O2)

result2 = calculation(a=K2, b=K3, operand=O2)
result2 = calculation(a=K1, b=result2, operand=O1)

m, M = min(result1, result2), max(result1, result2)

print(m)
print(M)