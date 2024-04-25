"""
문제
Kiedy Hektor zajmował się realizacją projektu HektorJudge, jego kolega Wiktor uznał, że życie nie powinno składać się wyłącznie z siedzenia przy komputerze i wybrał się na wycieczkę w góry. Kiedy wieczorem dotarł do schroniska ze zdziwieniem odkrył, że nie tylko on wpadł na pomysł spędzenia weekendu w górach - schronisko było pełne turystów!

W tej kryzysowej sytuacji kierownik schroniska był zmuszony zorganizować turystom nocleg na podłodze w głównej sali schroniska. Sala ma postać prostokąta złożonego z W*K kwadratowych pól ułożonych w prostokąt o wymiarach W wierszy na K kolumn. Każdy turysta zajmuje dokładnie dwa sąsiednie (albo w pionie albo w poziomie) pola. Ile turystów można maksymalnie ułożyć w sali o zadanych wymiarach tak, aby każde pole było zajęte maksymalnie przez jednego turystę? Wiktor, jako matematyk-informatyk natychmiast obliczył prawidłowy wynik.

입력
W pierwszej linii znajduje się liczba naturalna Z ( 1 <= Z <= 10 ) oznaczająca liczbę zestawów testowych. Następnie opisywane są kolejne zestawy.

Opis pojedynczego zestawu testowego składa się z jednej linii zawierającej dwie oddzielone pojedynczą spacją dodatnie całkowite W i K (1 <= W, K <= 1000).

출력
Dla każdego zestawu testowego należy w osobnej linii wypisać maksymalną liczbę turystów którzy mogą jednocześnie przenocować w sali schroniska. Kolejność wypisywanych odpowiedzi musi odpowiadać kolejności zestawów na wejściu.
"""

for Z in range(int(input())):
    W, K = map(int, input().split())
    
    print(W * K // 2)