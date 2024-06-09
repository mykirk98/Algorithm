"""
문제
7개의 자연수가 주어질 때, 이들 중 짝수인 자연수들을 모두 골라 그 합을 구하고, 고른 짝수들 중 최솟값을 찾는 프로그램을 작성하시오.

예를 들어, 7개의 자연수 13, 78, 39, 42, 54, 93, 86가 주어지면 이들 중 짝수는 78, 42, 54, 86이므로 그 합은 78 + 42 + 54 + 86 = 260 이 되고, 42 < 54 < 78 < 86 이므로 짝수들 중 최솟값은 42가 된다.

입력
입력은 T개의 테스트 데이터로 구성된다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터는 한 줄로 구성되어 있고, 7개의 자연수가 공백으로 구분되어 있다. 입력으로 주어지는 자연수는 1보다 크거나 같고, 100보다 작거나 같다. 7개의 자연수 중 적어도 하나는 짝수이다.

출력
각 테스트 데이터에 대해, 7개 자연수 중 짝수의 합과 최솟값을 공백으로 구분하여 한 줄에 하나씩 출력한다.
"""

# for T in range(int(input())):
#     numbers = list(map(int, input().split()))
    
#     min_value = 99999999
#     even_numbers = []
#     for number in numbers:
#         if number % 2 == 0:
#             even_numbers.append(number)

#     total = 0
#     for even_number in even_numbers:
#         total += even_number

#     for even_number in even_numbers:
#         if even_number < min_value:
#             min_value = even_number

#     print(total, min_value)

# 풀이 2
for T in range(int(input())):
    numbers = list(map(int, input().split()))
    min_value, total = 999999999, 0
    even_numbers = []
    
    for number in numbers:
        if number % 2 == 0:
            # even_numbers.append(number)
            total += number
            min_value = number if number < min_value else min_value
    print(total, min_value)