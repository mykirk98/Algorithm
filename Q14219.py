"""
문제
동혁이는 막대과자를 포장하는 아르바이트를 하고 있다. 막대과자는 그림과 같이 3 X1 직사각형 모양의 과자와 2 X 2 크기에 ㄴ자 모양의 과자가 있고, 동혁이는 이 과자를 포장 박스에 차곡차곡 넣으려 한다.



포장 박스의 크기는 n X m이고, 과자들은 부서지기 쉬우므로, 상자에 빈틈이 있으면 흔들려서 깨질 가능성이 있어, 상자를 빈틈없이 꽉 채우려고 한다. 아래 그림은 5 X 3의 박스를 채운 모습이다.



동혁이는 지금 막대과자와 포장 박스들을 가지러 갔다. 동혁이를 대신하여 포장 박스안에 과자들을 빈틈없이 넣을 수 있는지 확인해주자.

입력
박스의 가로 세로 길이 n,m이 주어진다.(1≤n,m≤500)

출력
과자를 빈틈없이 채울 수 있다면 “YES”, 채울 수 없다면 “NO”를 출력하시오.
"""

n, m = map(int, input().split())

if n < 3 and m < 3:
    print("NO")
else:
    if n % 3 == 0 or m % 3 == 0:
        print("YES")
    else:
        print("NO")