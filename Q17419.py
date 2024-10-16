"""
문제
🎶 DJ욱제는 비트에 몸을 맡기는 중이다. 🎶

DJ욱제는 비트에 심취한 나머지, 비트를 비틀어 제껴버리는 문제를 내 버렸다!

N자리 이진수 K가 주어진다. K가 0이 아닐 때까지 아래의 연산을 적용했을 때, 연산이 일어나는 횟수를 구하시오.

K = K-(K&((~K)+1))
아래는 위의 연산에 사용된 연산자에 대한 설명이다.

'+'는 산술 더하기 연산이다. (5 + 2 = 7)
'-'는 산술 빼기 연산이다. (5 - 2 = 3)
'&'는 비트 AND 연산이다. (1101 & 0111 = 0101)
'~'는 비트 NOT 연산이다. 켜진 비트를 끄고, 꺼진 비트를 켜는 연산이다. (~1101 = 0010)
입력
첫째 줄에 N이 주어진다.

둘째 줄에 N자리 이진수 K가 주어진다. K는 0으로 시작하지 않는다. 즉, leading zero는 없다.

출력
연산이 일어나는 횟수를 출력한다.
"""

N = int(input())

K = int(input(), base=2)

count = 0
while K != 0:
    count += 1
    K = K - (K & ((~K) + 1))

print(count)