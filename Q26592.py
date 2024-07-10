"""
문제
Your Math teacher asked you to write a program to help him generate homework solutions. The program will need to find the height of a triangle given its area and its base length.

Formula:

a = (h*b)/2 (a – area, b – base length, h – height)
입력
The first line will contain a single integer n that indicates the number of lines that follow. Each line will include the area and base length of a triangle with the two values separated by a single space.

area base
출력
For each input display the height of the triangle with 2 decimal places, in the following format:

The height of the triangle is #.## units
"""

for T in range(int(input())):
    area, length = map(float, input().split())

    # area = length * height / 2
    height = area / length * 2

    print(f"The height of the triangle is {height:.2f} units")