"""
문제
영선이와 효빈이는 슬라임을 합치는 게임을 하고 있다. 두 사람은 두 슬라임을 골라서 하나로 합쳐야 한다. 게임은 슬라임이 하나 남았을 때 끝난다.

모든 슬라임은 양수 크기를 가지고 있다. 두 슬라임 x와 y를 합쳤을 때, 합친 슬라임의 크기는 x+y가 된다. 또한, 슬라임을 합칠 때 마다 두 사람은 x*y 점수를 얻게 된다.

영선이와 효빈이가 얻을 수 있는 점수의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 슬라임의 개수 N (2 ≤ N ≤ 100)이 주어진다.

둘째 줄에는 슬라임의 크기가 주어진다. 크기는 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 영선이와 효빈이가 얻을 수 있는 점수의 최댓값을 출력한다.

"""

N = int(input())

slimes = list(map(int, input().split()))
score = 0

amount = min(slimes)
slimes.remove(amount)
while slimes != []:
    pick = min(slimes)
    slimes.remove(pick)
    
    score += amount * pick
    amount += pick

print(score)