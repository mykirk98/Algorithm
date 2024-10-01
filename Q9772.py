"""
문제
Given the coordinates (x,y) of some points in 2-dimensional plane, find out which quadrant(Q1-Q4) the points are located. If a point is located on X-axis or Y-axis, print out AXIS instead.



입력
Each line contains a pair of real numbers which is the coordinate of a point. Input is terminated by 0 0.

출력
Print out in each line Q1, Q2, Q3, Q4 or AXIS for each point.
"""

while True:
    x, y = map(float, input().split())
    
    if x > 0 and y > 0:
        print('Q1')
    elif x < 0 and y > 0:
        print('Q2')
    elif x < 0 and y < 0:
        print('Q3')
    elif x > 0 and y < 0:
        print('Q4')
    else:
        print('AXIS')
    
    if x == y == 0:
        break