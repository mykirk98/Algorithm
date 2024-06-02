"""
문제
En route to Rigel 7, Chief Engineer Geordi Laforge and Data were discussing favorite numbers. Geordi exclaimed he preferred Narcissistic Numbers: those numbers whose value is the same as the sum of the digits of that number, where each digit is raised to the power of the number of digits in the number.

Data agreed that Narcissistic Numbers were interesting, but not as good as his favorite: Perfect Numbers. Geordi had never heard of a Perfect Number, so Data elaborated, “A positive integer is said to be Perfect if it is equal to the sum of its positive divisors less than itself. For example, 6 is Perfect because 6 = 1 + 2 + 3.”

Geordi began thinking about an algorithm to determine if a number was Perfect, but did not have the raw computing ability of Data. He needs a program to determine if a given number is Perfect.

Help Geordi write that program.

입력
Input consists of a single entry per line. Each line contains a single positive integer n, where 2 < n < 100000 for each case. A line containing -1 denotes the end of input and should not be processed.

출력
For each case, determine whether or not the number is Perfect. If the number is Perfect, display the sum of its positive divisors less than itself. The ordering of the terms of the sum must be in ascending order. If a number is not Perfect, print “<NUM> is NOT perfect.” where <NUM> is the number in question. There must be a single space between any words, symbols, or numbers in all output, with the exception of the period at the end of the sentence when a number is not perfect.
"""

while True:
    n = int(input())
    if n == -1:
        break
    
    divisor = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            divisor.append(n // i)
    divisor.remove(n)
    divisor.sort()
    
    if sum(divisor) == n:
        print(f"{n} =", end=" ")
        for i in divisor:
            print(f"{i}",end=" ")
            if i != divisor[-1]:
                print(f"+", end=" ")
    else:
        print(f"{n} is NOT perfect.")