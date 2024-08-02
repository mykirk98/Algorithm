"""
문제
연속한 소수 p와 p+n이 있을 때, 그 사이에 있는 n-1개의 합성수(소수나 1이 아닌 양의 정수)는 길이가 n인 소수 사이 수열라고 부른다.

양의 정수 k가 주어졌을 때, k를 포함하는 소수 사이 수열의 길이를 구하는 프로그램을 작성하시오. k를 포함하는 소수 사이 수열이 없을 때는 길이가 0이다.

예를 들어, 소수 23과 29의 소수 사이 수열은 {24, 25, 26, 27, 28}이고, 길이는 6이다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 테스트 케이스는 한 줄로 이루어져 있고, 한 줄에 정수 k가 주어진다. 각각의 정수는 1보다 크고, 100000번째 소수(1299709)와 작거나 같다.

출력
각각의 테스트 케이스에 대해서 k가 합성수라면 k를 포함하는 소수 사이 수열의 길이를 출력한다. 그렇지 않으면 0을 출력한다.
"""

def is_prime(n):
    flag = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            flag = False
            return flag
    return flag



for T in range(int(input())):
    k = int(input())
    if is_prime(k) == True:
        print(0)
        continue
    
    min_prime, max_prime = None, None
    min_num, max_num = k, k
    
    while min_prime != True:
        min_num -= 1
        min_prime = is_prime(min_num)

    while max_prime != True:
        max_num += 1
        max_prime = is_prime(max_num)

    print(max_num - min_num)