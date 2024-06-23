"""
문제
Kozik pragnie zostać koszykarzem. Po rozmowie z trenerem okazało się, że jest za niski. Kozik jest jednak tak zdeterminowany, że chce spełnić wymagania trenera, nawet jeśli okazałoby się to oszustwem. Wpadł więc na genialny pomysł robienia sobie guzów na głowie, aż osiągnie wymagany wzrost. Zauważył, że przy każdym uderzeniu guz się powiększa o m cm. Kozik zastanawia się ile minimalnie razy będzie musiał się uderzyć.

입력
W pierwszej linii wejścia 3 liczby całkowite: k, w, m (1 ≤ k ≤ 200, 1 ≤ w, m ≤ 109), oznaczające odpowiednio wysokość Kozika, wymaganą przez trenera wysokość oraz wartość powiększania się guza po każdym uderzeniu.

출력
Pierwszy i jedyny wiersz wyjścia powinien zawierać jedną liczbę całkowitą równą minimalnej liczbie uderzeń, które musi wykonać Kozik.
"""

k, w, m = map(int, input().split())

differece = w - k

if differece % m == 0:
    print(f"{(differece / m):.0f}")
else:
    print(f"{(differece / m) + 1:.0f}")