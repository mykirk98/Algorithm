"""
문제
You have hired someone to help you with inventory on the farm. Unfortunately, the new cowhand has very limited math skills, and they are having trouble summing two numbers. Write a program to determine if the cowhand is adding these numbers correctly.

입력
The first and only line of input contains a string of the form:

a + b = c

It is guaranteed that a, b, and c are single-digit integers. The input line will have exactly 9 characters, formatted exactly as shown, with a single space separating each number and arithmetic operator.

출력
Print on a single line, YES if the sum is correct; otherwise, print NO.
"""

form = list(input().split())

print("YES" if int(form[0]) + int(form[2]) == int(form[4]) else "NO")