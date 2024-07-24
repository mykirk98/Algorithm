"""
문제
Bajtuś znalazł w lesie 3 patyki. Teraz chciałby wiedzieć, czy może z nich zbudować trójkąt prostokątny lub równoboczny. Bajtuś nie może łamać patyków, może je wykorzystać tylko w całości.

입력
Pierwszy wiersz wejścia zawiera trzy liczby całkowite a, b, c (1 ≤ a, b, c ≤ 1000), oznaczające odpowiednio długości pierwszego, drugiego i trzeciego patyka.

출력
Pierwszy i jedyny wiersz wyjścia powinien zawierać jedną liczbę: 0 - jeśli Bajtuś nie może zbudować, ani trójkąta prostokątnego ani równobocznego, 1 - jeśli Bajtuś może zbudować tylko trójkąt prostokątny, 2 - jeśli Bajtuś może zbudować tylko trójkąt równoboczny,
"""

abc = list(map(int, input().split()))

c = max(abc)
abc.remove(c)

a, b = abc[0], abc[1]

if a == b == c:
    print(2)
elif a ** 2 + b ** 2 == c ** 2:
    print(1)
else:
    print(0)