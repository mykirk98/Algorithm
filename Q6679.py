"""
문제
싱기한 네자리 숫자란, [1000,9999]인 10진수 숫자중에서,  다음의 조건을 만족하는 숫자를 말한다.

숫자를 10진수, 12진수, 16진수로 나타낸 다음, 각각의 숫자에 대해, 각 숫자의 자리수를 더했을 때, 세 값이 모두 같아야 한다.
여러분은 싱기한 네자리 숫자를 모두 출력해야 한다.

입력
입력은 주어지지 않는다.

출력
싱기한 네자리 숫자를 오름차순으로 한줄에 하나씩 출력한다.
"""
def exchange(n, total, base):
    if n % base == 0 and n // base == 0:
        return total
    
    total += n % base
    return exchange(n // base, total, base)


base = [10, 12, 16]


for number in range(1000, 10000):
    arr = []
    for b in base:
        total = 0
        arr.append(exchange(n=number, total=total, base=b))

    if arr[0] == arr[1] == arr[2]:
        print(number)