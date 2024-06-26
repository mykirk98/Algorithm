"""
문제
Робинзон Крузо на необитаемом острове отмечает дни стене своей хижины.

Каждый день он ставит зарубку, которую будем обозначать английской буквой <<I>>, а раз в 5 дней зачеркивает четыре предыдущие зарубки, получая символ, который мы обозначим как <<V>>.

Какая запись получится на стене хижины Робинзона на 
$n$-й день?

입력
На ввод подается одно число 
$n$ (
$1 \le n \le 10\,000$).

출력
Выведите запись, которая получится на стене хижины Робинзона на 
$n$-й день.
"""

N = int(input())

V = N // 5
I = N % 5

print('V' * V + 'I' * I)