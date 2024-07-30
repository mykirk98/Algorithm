"""
문제
Niech n będzie nieujemną liczbą całkowitą. Liczbę n! (czytaj n-silnia) definiuje się następująco. Jeśli n ≤ 1, to n! = 1. Dla n > 1, n! jest równe iloczynowi wszystkich liczb od 1 do n, czyli n! = 1 * 2 * ... * n. Na przykład 4! = 1 * 2 * 3 * 4 = 24.

Napisz program, który

wczyta ze standardowego wejścia nieujemną liczbę całkowitą n,
policzy cyfrę jedności w zapisie dziesiętnym liczby n!,
wypisze wynik na standardowe wyjście.
입력
Pierwszy i jedyny wiersz standardowego wejścia zawiera dokładnie jedną nieujemną liczbę całkowitą n, 0 ≤ n ≤ 30 000.

출력
W pierszym i jedynym wierszu standardowego wyjścia Twój program powinien zapisać dokładnie jedną cyfrę równą cyfrze jedności w zapisie dziesiętnym liczby n!.

"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
    
    return result

n = int(input())

output = str(factorial(n))[-1]

print(output)