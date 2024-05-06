"""
문제
W Bajtocji noszenie skarpetek o różnych kolorach i wzorach przestało już być modne. Teraz nastała moda na noszenie wyłącznie dwóch skarpetek białych lub dwóch skarpetek czarnych.

Bajtazar, który zawsze stara się nadążać za trendami w modzie, zakupił dużo pojedynczych skarpetek (białych i czarnych). Chciałby wiedzieć ile jednokolorowych (albo białych albo czarnych) par skarpetek uda mu się skompletować.

Ponieważ Bajtazar nie radzi sobie za dobrze ze zliczaniem swoich skarpetek, zwrócił się do Ciebie z prośbą o pomoc. Napisz program, który wczyta ciąg opisujący skarpetki Bajtazara i wyznaczy liczbę jednokolorowych par skarpetek, które można z nich skompletować.

입력
W pierwszym (jedynym) wierszu wejścia znajduje się niepusty ciąg liter B oraz C oznaczających kolory kolejnych skarpetek Bajtazara (B oznacza skarpetkę białą, a C skarpetkę czarną).

Długość ciągu nie przekracza 1 000 000 znaków.

출력
W pierwszym (jedynym) wierszu wyjścia należy wypisać jedną nieujemną liczbę całkowitą – liczbę par skarpetek jednokolorowych, jakie można stworzyć ze skarpetek opisanych na wejściu.
"""

W = input()

B = W.count('B')
C = W.count('C')

print(B // 2 + C // 2)