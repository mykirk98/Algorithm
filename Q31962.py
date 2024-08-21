"""
문제
정올이는 수업에 지각하지 않기 위해 학교에 
$X$분 이내로 도착해야 한다. 학교로 이동하려면 정류장에 정차하는 
$N$개의 버스 중 하나를 선택하여 탑승해야 한다.

게으른 정올이는 최대한 늦게 버스를 타기 위해서 
$N$개의 버스의 정보를 찾아보았다. 각 버스가 지금부터 몇 분 후에 정류장에서 출발하며, 정류장에서 출발한 버스가 학교에 도착하기 위해 몇 분이 걸리는지 알아낼 수 있었지만, 어떤 버스를 타고 학교에 갈지 아직 결정하지 못했다.

정올이를 위해서 학교에 지각하지 않는 시각에 도착하는 버스 중에서, 가장 늦게 출발하는 버스가 출발할 때까지 걸리는 시간을 구해주자. 학교에 지각하지 않도록 버스를 선택하는 방법이 없을 수도 있다.

입력
첫 번째 줄에 
$N$과 
$X$가 공백을 하나 사이에 두고 주어진다.

두 번째 줄부터 
$N$개의 줄에 걸쳐, 한 줄에 하나씩 정류장에서 버스가 출발할 때까지 걸리는 시간 S와, 버스가 정류장에서 학교까지 가는 데 걸리는 시간 
$T$가 공백을 하나 사이에 두고 주어진다.

출력
학교에 
$X$분 이내로 도착할 수 없다면, 
$-1$을 출력한다.

학교에 
$X$분 이내로 도착할 수 있다면, 가장 늦게 출발하는 버스가 출발할 때까지 걸리는 시간을 출력한다.
"""

# N : 버스 개수
# X : 학교에 도착해야하는 시간

# N, X = map(int, input().split())

# start = 0
# maximum = 0
# for n in range(N):
#     S, T = map(int, input().split())
#     if S + T > maximum:
#         if S + T <= X:
#             maximum = S + T
#             start = S

# if start == 0:
#     print(-1)
# else:
#     print(start)

N, X = map(int, input().split())
busInfo = []
for _ in range(N):
    S, T = map(int, input().split())
    busInfo.append([S, T])

busInfo.sort(key=lambda x: -x[0])

arriveCheck = False
for k, d in busInfo:
    if k + d > X:
        continue
    else:
        arriveCheck = True
        takeTime = k  # 걸리는 시간
        break

if arriveCheck:
    print(takeTime)
else:
    print(-1)