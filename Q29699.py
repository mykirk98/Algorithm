"""
문제
화은이는 제3회 SMUPC를 맞이하여 환영의 의미로 "WelcomeToSMUPC"가 반복적으로 적혀 있는 라벨지를 프린트했다. 라벨지에는 공백 없이 글자들이 이어져 있고 "WelcomeToSMUPC"의 마지막 글자인 C 이후에는 W부터 다시 "WelcomeToSMUPC"가 반복된다. 
$N$번째 글자가 있는 곳까지 라벨지를 자르려 할 때, 
$N$번째에는 어떤 글자가 있을지 구해보자.


[ 
$N$=15 일 때 라벨지를 자르는 위치 ]
입력
첫째 줄에 
$N$(
$ 1 \leq N \leq 1\,000\,000$)이 주어진다.

출력
첫째 줄에 
$N$번째에 해당하는 글자를 출력한다.
"""

N = int(input()) % 14

word = 'WelcomeToSMUPC'

print(word[N-1])