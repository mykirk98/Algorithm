"""
문제
창영이는 여러 가지 진법을 공부하고 있다. 창영이는 어제 2진법을 배웠고, 오늘은 8진법을 배웠다. 이제, 2진법 수를 8진법 수로 변환하려고 한다.

창영이가 사용한 방법은 다음과 같다.

2진수의 길이가 3으로 나누어 떨어질 때 까지 수의 앞에 0을 붙인다.
그 다음, 3자리씩 그룹을 나눈다.
아래의 표를 참고해 8진수로 바꾼다.
2진수가 주어졌을 때, 창영이가 사용한 방법을 이용해 8진수로 바꾸는 프로그램을 작성하시오.

000	0
001	1
010	2
011	3
100	4
101	5
110	6
111	7
입력
첫째 줄에 2진수가 주어진다. 이 수는 100자리 이내이고, 첫 번째 자리는 1이다.

출력
첫째 줄에 8진수를 출력한다.
"""

def dec_to_bin(n:int):
    number = ''
    while n / 2 != 0:
        number += str(n % 2)
        n //= 2
    
    return number[::-1]

def bin_to_dec(binary:str):
    number = 0
    for i, b in enumerate(binary[::-1]):
        number +=int(b) * 2 ** i

    return number

def dec_to_oct(n:int):
    octal = ''
    while n / 8 != 0:
        octal += str(n % 8)
        n //= 8
    
    return octal[::-1]

binary_number = input()

decimal_number = bin_to_dec(binary_number)

octal_number = dec_to_oct(decimal_number)

print(octal_number)