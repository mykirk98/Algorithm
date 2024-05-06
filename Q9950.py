"""
문제
My young son is struggling with his maths homework, can you help him please? He is working on the area of a rectangle – you know, area = length x width. His teacher has given him a table of lengths, widths and areas. Each row on the table has one of the 3 values missing; my son has to work out the missing value and write it in the table such that the values on each line represent the length, width and area of one rectangle.

입력
Input is a series of lines, each containing 3 integers, l, w, and a ( 0 ≤ l w ≤100, 0 ≤ a ≤ 10,000) representing the length, width and area of a rectangle in that order. The integers are separated by a single space. In each row, only one of the values has been replaced by a zero. The final row contains 0 0 0 and should not be processed.

출력
Output is the same series of lines but with the zero in each line replaced by the correct value for the length, width or area as appropriate. The new value is always an integer.
"""

while True:
    l, w, a = map(int, input().split())
    
    if l == w== a == 0:
        break
    
    if l == 0:
        l = a // w
    elif w == 0:
        w = a // l
    elif a == 0:
        a = l * w
    
    print(l, w, a)