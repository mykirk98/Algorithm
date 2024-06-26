"""
문제
정수 X가 주어진다. 정수 X는 항상 8진수, 10진수, 16진수 중에 하나이다.

8진수인 경우에는 수의 앞에 0이 주어지고, 16진수인 경우에는 0x가 주어진다.

X를 10진수로 바꿔서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 X가 주어진다. X는 10진수로 바꿨을 때, 1,000,000보다 작거나 같은 자연수이다. 16진수인 경우 알파벳은 소문자로만 이루어져 있다.

출력
첫째 줄에 입력받은 X를 10진수로 바꿔서 출력한다.
"""

X = input()

if X[0] == '0':
    if X[1] == 'x': # 16진수
        print(int(X[2:], base=16))
    else: # 8진수
        print(int(X[1:], base=8))
else: # 10진수
    print(X)