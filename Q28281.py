"""
문제
 
$N$일 뒤는 동원이의 생일이다. 축하해 주자!

준원이는 동원이에게 생일 선물로 양말을 
$2X$개 선물하려 한다. 양말은 시장에서 살 것이다. 연속한 이틀에 걸쳐서, 준원이는 매일 시장에서 양말을 
$X$개씩 사서 트럭에 담아올 것이다.

시장에서 양말의 가격은 날마다 다를 수 있다. 오늘부터 
$i$번째 날에, 양말은 하나에 
$A_i$원이다.

동원이의 생일까지 
$N$일 남았다! 남은 
$N$일 가운데 연속한 이틀에 걸쳐 양말 
$2X$개를 사는 데 드는 최소 비용은?

입력
첫째 줄에 
$N$과 
$X$가 공백을 사이에 두고 주어진다.

둘째 줄에 
$N$일간 양말의 가격 
$A_1, A_2, \cdots, A_N$이 공백을 사이에 두고 주어진다.

출력
연속한 이틀에 걸쳐 하루에 양말을 
$X$개씩 구매하는 방법으로, 양말 
$2X$개를 사는 데 드는 최소 비용을 출력한다.
"""

N, X = map(int, input().split())
A = list(map(int, input().split()))

min_value = 2000
for i in range(len(A)-1):
    if A[i] + A[i+1] < min_value:
        min_value = A[i] + A[i+1]

print(min_value * X)