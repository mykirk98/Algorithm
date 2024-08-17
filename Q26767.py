"""
문제
Mała Bajtynka lubi liczyć, a szczególnie uwielbia liczby 7 i 11. Mimo najlepszych starań nauczycieli, Bajtynka uroczyście celebruje, zarówno w mowie, jak i na piśmie, każdą napotkaną liczbę podzielną przez 7, zamiast jej nazwy wykrzykując (albo pisząc) Hurra!. Liczenie Bajtynki może więc wyglądać tak:

. . . , 5, 6, Hurra!, 8, 9, . . .

albo tak:

. . . , 12, 13, Hurra!, 15, 16, . . .

Podobnie każda liczba podzielna przez 11 zastępowana jest okrzykiem Super! (na przykład: . . . , 31, 32, Super!, 34, . . . ). Jeśli zaś Bajtynka napotka liczbę, która jest podzielna zarówno przez 7, jak i 11, zamiast niej woła Wiwat! – jest to nieco archaiczne, ale historia jest, zaraz po informatyce, ulubionym przedmiotem Bajtynki.

Spraw Bajtynce prezent na urodziny – napisz program, który w jej imieniu doliczy do dużych liczb!

입력
Twój program powinien wczytać z wejścia jedną liczbę całkowitą N. Liczba będzie równa co najmniej 1 i co najwyżej 1 000 000.

출력
Wypisz kolejne liczby od 1 do N tak, jak napisałaby je Bajtynka. Każdą liczbę wypisz w oddzielnym wierszu.
"""

numbers = list(range(1, int(input())+1))

for number in numbers:
    if number % 77 == 0:
        print("Wiwat!")
    elif number % 7 == 0:
        print("Hurra!")
    elif number % 11 == 0:
        print("Super!")
    else:
        print(number)