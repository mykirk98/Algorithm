"""
문제
양의 정수 n의 각 자리수의 제곱의 합을 계산한다. 그렇게 해서 나온 합도 각 자리수의 제곱의 합을 계산한다. 이렇게 반복해서 1이 나온다면, n을 상근수라고 한다.

700은 상근수이다.

72 + 02 + 02 = 49
42 + 92 = 97
92 + 72 = 130
12 + 32 + 02 = 10
12 + 02 = 1
2는 상근수가 아니다.

22 = 4
42 = 16
12 + 62 = 37
32 + 72 = 58
52 + 82 = 89
82 + 92 = 145
12 + 42 + 52 = 42
42 + 22 = 20
22 + 02 = 4
42 = 16
... 끝나지 않는다
소수는 1과 자기자신을 제외하고 약수가 없는 수이다. 2, 3, 5, 7, 11, 13, 17, 19, ... 는 소수이다.

소수상근수는 소수이면서 상근수인 숫자이다. 7, 13, 19, ... 는 소수 상근수이다.

n이 주어졌을 때, n보다 작거나 같은 모든 소수상근수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n (10 ≤ n ≤ 1000000)이 주어진다.

출력
n보다 작거나 같은 소수상근수를 한 줄에 하나씩 오름차순으로 출력한다.
"""

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

N = int(input())

prime = [2, 3, 5, 7]

for n in range(10, N+1):
    if isPrime(n=n) == True:
        prime.append(n)

for p in prime:
    num = str(p)
    while num != '4':
        total = 0
        for i in num:
            total += int(i) ** 2
        num = str(total)
        
        if num =='1':
            print(p)
            break