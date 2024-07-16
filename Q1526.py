"""
문제
은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.

N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. N은 4보다 크거나 같고 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 N보다 작거나 같은 금민수 중 가장 큰 것을 출력한다.
"""

N = int(input())        # 4 <= N <= 1,000,000

flag = None
for number in range(N, 3, -1):
    for n in str(number):
        if n in ('4', '7'):
            flag = True
        else:
            flag = False
            break
    if flag:
        print(number)
        break