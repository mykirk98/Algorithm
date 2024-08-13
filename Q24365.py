"""
문제
На три цветя, подредени в редица на разстояние през 1 метър, са кацнали пчели. На лявото цвете пчелите не са повече от тези на средното, а на средното не са повече от пчелите, кацнали на дясното цвете.

Ръководител на всички е пчеличката Мая. Тя пресметнала, че ако определи някои от пчелите да се преместят, то на трите цветя ще има по равен брой пчели. За съжаление, работливите пчели трябва да пестят силите си. Затова Мая иска първо да изчисли минималния брой метри, които може да се прелетят и след това вече ще определи коя пчела на кое цвете да се премести.

За да помогнете на пчеличката Мая, напишете програма bee, която извежда този минимален брой метри.

입력
От първия ред на стандартния вход се въвеждат три цели числа А, В и C - брой на пчелите съответно на лявото, средното и дясното цвете. Числата са разделени с по един интервал.

출력
На един ред на стандартния изход програмата трябва да изведе едно цяло число – минималния общ брой прелетени метри от пчелите.
"""

A, B, C = map(int, input().split())

average = (A + B + C) // 3
total = 0

total += C - average
B += C - average

total += B - average
A += B - average

print(total)
print(A, B, C)