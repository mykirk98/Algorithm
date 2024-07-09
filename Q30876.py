"""
문제
Southern Fuegian Railway는 세상에서 가장 남쪽에 있는 철도이다.

Southern Fuegian Railway는 
$x$축의 양의 방향을 동쪽으로 하는 
$2$차원 좌표평면으로 나타내어진다.

Southern Fuegian Railway는 
$N$개의 역과 역 사이를 잇는 
$N-1$개의 철로로 구성되어 있다. 
$i$번째 역은 
$(x_i,y_i)$에 있으며, 
$j$번째 철로는 
$j$번 역과 
$j+1$번 역 사이를 잇는 선분이다. 
$(1 \le i \le N;$ 
$1 \le j \le N-1)$ 

Southern Fuegian Railway를 보러 간 선아는 세상에서 가장 남쪽에 있는 철도가 지나는 가장 남쪽 점이 어디일지 궁금해졌다.

입력
첫 번째 줄에 역의 개수 
$N$이 주어진다. 
$(1\le N\le 1\, 000)$ 

두 번째 줄부터 
$N$개의 줄에 걸쳐서, 역의 좌표를 의미하는 두 정수 
$x_i,y_i$가 공백으로 구분되어 주어진다. 
$(|x_i|,|y_i|\le 1\, 000)$ 

두 역이 같은 위치에 있는 경우는 주어지지 않는다.

출력
첫 번째 줄에 Southern Fuegian Railway가 지나는 가장 남쪽에 있는 점의 
$x$좌표와 
$y$좌표를 공백으로 구분하여 출력한다. 이 점이 유일한 경우만 입력으로 주어진다.
"""

# x_south = 0
# y_south = 1000
# for N in range(int(input())):
#     x, y = map(int, input().split())

#     if y < y_south:
#         x_south, y_south = x, y

# print(x_south, y_south)

dots = []

for _ in range(int(input())):
    x, y = map(int, input().split())
    dots.append([y, x])

print(*(min(dots)[::-1]))