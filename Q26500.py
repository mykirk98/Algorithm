"""
문제
We will call the distance between any two values on the number line the absolute line distance. Given two values, find the absolute line distance and output it, rounded and formatted to one place of precision.

입력
The first line contains a single positive integer, n, indicating the number of data sets. Each data set is on a separate line and contains two values on the number line, separated by a single space.

출력
The absolute line distance between the two points, rounded to the nearest tenth, and print exactly one decimal digit.
"""

for n in range(int(input())):
    a, b = map(float, input().split())
    
    print(f"{abs(b - a):.1f}")