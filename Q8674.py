"""
문제
Mama przyniosła Piotrusiowi i Pawełkowi tabliczkę czekolady o wymiarach a i b. Chłopcy chcą podzielić tabliczkę za pomocą jednego prostego łamania, wzdłuż kostek pionowych lub poziomych. Chłopcy chcą podzielić tabliczkę jak najbardziej sprawiedliwie, czyli tak, aby różnica pomiędzy kawałkami, które przypadną na każdego z nich, była jak najmniejsza.

입력
W pierwszym i jedynym wierszu wejścia znajdują się dwie liczby całkowite a, b (1 ≤ a, b ≤ 232), oznaczające odpowiednio liczbę kostek znajdujących się w każdym wierszu oraz każdej kolumnie tabliczki czekolady.

출력
W pierwszym i jedynym wierszu wyjścia powinna się znaleźć jedna liczba całkowita, równa różnicy pomiędzy kawałkami, które dostaną chłopcy.
"""

a, b = map(int, input().split())

if a % 2 == 0 or b % 2 == 0:
    print(0)
else:
    print(min(a, b))