"""
문제
Миша живет на 
$n$-м этаже. Когда Миша заходит в подъезд, он смотрит, на каком этаже в этот момент находится лифт и решает, вызвать лифт или пойти по лестнице.

Сегодня лифт находится на 
$k$-м этаже. Миша заходит в подъезд на 1 этаже. Он поднимается на один этаж за 
$a$ секунд. Лифт перемещается на один этаж за 
$b$ секунд. Временем входа в лифт и выхода из лифта, а также перемещения к лестнице и обратно можно пренебречь.

Помогите Мише принять решение, выведите, за какое время он попадет на свой этаж на лифте и по лестнице, соответственно.

입력
На ввод подаются целые числа: 
$n$, 
$k$, 
$a$ и 
$b$.

 
$2 \le n \le 100$, 
$1 \le k \le 100$, 
$1 \le a, b \le 1000$.

출력
Выведите два целых числа: время, за которое Миша поднимется на свой этаж на лифте, и время, за которое Миша поднимется на свой этаж по лестнице.

n : 미샤가 사는 층
k : 엘리베이터가 정지해 있는 층
a : 미샤가 한 층 올라가는 데 걸리는 시간
b : 엘리베이터가 한 층 이동하는데 걸리는 시간
"""

n, k, a, b = map(int, input().split())

EV = (n + k - 2) * b
walk = (n - 1) * a

print(EV, walk)