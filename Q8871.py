"""
문제
Wyobraźmy sobie przez chwilę, że w tym roku konkurs SKI'10 składa się z n punktowanych rund i jednej rundy próbnej. Ile zgodnie z regulaminem może się pojawić zadań w czasie całych zawodów?

입력
W pierwszej i jedynej linii znajduje się liczba naturalna n (1<=n<=1000).

출력
Twój program powinien wypisać dwie liczby oddzielone pojedynczym odstępem. Pierwsza liczba to minimalna liczba zadań jaka może pojawić się podczas n rund punktowanych i jednej rundy próbnej w trakcie SKI'10. Druga liczba to maksymalna liczba zadań w tym konkursie.
"""

n = int(input())

min_round = (n + 1) * 2
max_round = (n + 1) * 3

print(min_round, max_round)