"""
문제
Dave has a collection of N interesting pebbles. He wishes to arrange them in rows and columns in such a way that the sum of number of rows and number of columns needed is minimal possible. Write a program that will help Dave to find such numbers. 

입력
The first and only line of input file contains a natural number N (1 ≤ N ≤ 100), the number of pebbles to be arranged. Arrangement needs not to be regular in any sense – some places in a row may be empty.

출력
The first and only line of output file must contain number of rows and number of columns separated by one space.

Note: A solution needs not to be unique.
"""

N = int(input())
rows, columns = 1, 1

while rows * columns < N:
    if rows > columns:
        columns += 1
    else:
        rows += 1

print(rows, columns)