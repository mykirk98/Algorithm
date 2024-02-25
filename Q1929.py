"""
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
"""

M, N = map(int, input().split())
# M, N = 3, 16

for number in range(M, N+1):
    if number == 1:
        continue
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            break
    else:
            # if i == int(number ** 0.5):
        print(number)

# m,n=map(int,input().split())

# for i in range(m,n+1):
#     if i==1:#1은 소수가 아니므로 제외
#         continue
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0: #약수가 존재하므로 소수가 아님
#             break   #더이상 검사할 필요가 없으므로 멈춤
#     else:
#         print(i)

"""
반복문을 돌린다. 범위는 2부터 int(i**0.5)+1까지이다.
특정 수의 제곱근을 구해, 그 제곱근까지의 약수를 구하면 해당 약수를 포함하는 수를 모두 제거할 수 있다.
이렇기 때문에 범위를 위와같이 설정해주었다.
"""