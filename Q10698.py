"""
문제
Ahmed Aly was the chief judge for the last Arab Collegiate Programming Contest, and he will be the chief judge for the next one also. He was an ACM ICPC world finalist in Oralndo 2011, and currently he is a software engineer at Google.

During the last ACPC contest, it was the first time that the chief judge didn’t not attend the contest, and this was because his son Omar was expected to be born a few days before or after the contest (he was born 10 days after the contest), so he could not travel to Jordan.

Now his son Omar is old enough (9 months old) to start learning programming. His first program was very simple, just a program to add or subtract two numbers, and he needs your help to check if his program is correct or not.

입력
Your program will be tested on one or more test cases. The first line of the input will be a single integer T, the number of test cases (1 ≤ T ≤ 100). Followed by T lines, each test case is a single line containing an equation in the following format “X O Y = Z”, where X, Y and Z are positive integers (1 ≤ X,Y,Z ≤ 100) and O is either ‘+’ or ‘-’ (without the quotes).

출력
For each test case print a single line containing “Case n:” (without the quotes) where n is the test case number (starting from 1) followed by a space then “YES” (without the quotes) if the equation is correct or “NO” (without the quotes) if the equation is wrong.
"""

for T in range(int(input())):
    expression = input().split()
    if expression[1] == '+':
        if int(expression[0]) + int(expression[2]) == int(expression[4]):
            print(f"Case {T+1}: YES")
        else:
            print(f"Case {T+1}: NO")
    elif expression[1] == '-':
        if int(expression[0]) - int(expression[2]) == int(expression[4]):
            print(f"Case {T+1}: YES")
        else:
            print(f"Case {T+1}: NO")