"""
문제
이 문제는 
$x_0$와 
$N$의 제한을 제외하고 특별한 큰 분수와 같은 문제이다.

NLCS에는 분수가 많다.

분수에서 나오는 물의 높이는 특정한 규칙에 따라 변화하는데, 어떤 정수 시각 
$t$에서의 분수의 높이가 정수 
$x_t$일 때, 
$x_{t+1}$는 
$x_t$가 짝수라면 
 
$\lfloor \frac{x_t}{2} \rfloor \oplus 6$, 
$x_t$가 홀수라면 
$(2 \cdot x_t) \oplus 6$과 같다.

 
$0$초에서의 분수의 높이가 주어졌을 때, 
$N$초에서의 분수의 높이를 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 
$0$초에서의 분수의 높이 
$x_0$와 
$N$이 주어진다. 
$x_0$와 
$N$은 모두 정수이다.

출력
첫 번째 줄에 
$N$초에서의 분수의 높이를 출력한다.
"""

x0, N = map(int, input().split())

x_list = [x0]

for i in range(N):
    if x_list[i] % 2 == 0:
        x_list.append((x_list[i] // 2) ^ 6)
    else:
        x_list.append((2 * x_list[i]) ^ 6)
        
print(x_list[-1])