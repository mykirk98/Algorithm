"""
문제
A cuboid is a 3 dimensional shape in which each of the six faces is a rectangle.
Sally Jones, a primary school teacher, is giving her pupils some practice at calculating the volume of a cuboid.
I am sure you remember that volume = length x width x height.

Sally has given her pupils a table of lengths, widths, heights and volumes.
Each row on the table has one of the 4 values missing;
    the pupils have to work out the missing value and write it in the table such that the values on each line represent the length, width, height and volume of one cuboid. 

입력
Input is a series of lines, each containing 4 integers, l, w, h and v representing the length, width height and volume of a cuboid in that order.
The integers are separated by a single space. 0 < l, w, h <100, 0 < v < 100,000.
In each row, one of the values has been replaced by a zero. The final row contains 0 0 0 0 and should not be processed. 

출력
Output is the same series of lines but with the zero in each line replaced by the correct value for length, width, height or volume as appropriate.
The new value is always an integer.
"""

while True:
    l, w, h, v = map(int, input().split())
    if l == w == h == v == 0:
        break
    
    if l == 0:
        l = v // w // h
    elif w == 0:
        w = v // l // h
    elif h == 0:
        h = v // l // w
    elif v == 0:
        v = l * w * h
    
    print(l, w, h, v)