"""
문제


브실이의 친구들이 다 GOSU가 되자 자신과 실력이 비슷한 새로운 친구들을 사귀려고 한다. 주변을 아무리 둘러봐도 전부 GOSU뿐인 이곳에서 브실이는 겨우겨우 자신과 실력이 비슷한 사람들을 모았다. 놀랍게도 이 사람들이 푼 문제 수는 전부 다르며, 푼 문제 수가 적은 순서대로 배열했을 시 각각 
$A, A+1, \cdots, B$ 문제를 풀었다고 한다.

새로운 친구를 사귈 생각에 들떠 있던 브실이는 이내 차가운 현실과 마주쳤다. 이들 중 몇 명은 브실이와 푼 문제 차이가 너무 많이 났기 때문이다. 그래서 브실이는 본인과 푼 문제 수 차이가 
$X$보다 작거나 같은 사람만 친구의 자격을 갖추었다고 생각한다. 브실이가 푼 문제 수가 
$K$개일 때, 브실이의 친구가 될 수 있는 사람의 수를 구해보자!

입력
첫 번째 줄에 
$A$와 
$B$가 공백으로 구분되어 주어진다. 
$(1\le A \le B \le 10\,000)$ 

두 번째 줄에 브실이가 푼 문제 수 
$K$와 양의 정수 
$X$가 공백으로 구분되어 주어진다. 
$(1\le K, X \le 10\,000)$ 

출력
브실이의 친구가 될 수 있는 사람의 수를 출력한다.

친구가 될 수 있는 사람이 단 한 명도 없다면 IMPOSSIBLE을 출력한다.
"""

A, B = map(int, input().split())
K, X = map(int, input().split())

person = 0
for i in range(K - X, K + X + 1):
    if A <= i <= B:
        person +=1

if person == 0:
    print("IMPOSSIBLE")
else:
    print(person)