"""
문제
A right triangle or right-angled triangle is a triangle in which one angle is a
right angle (that is, at 90 degrees angle). The largest side of such a triangle is called hypotenuse. The relation between the sides of the triangle is

c2=a2+b2, Where c is the hypotenuse

Given 3 sides of a triangle, your task is to determine whether the given triangle is a right triangle or not. 

입력
The first line has a positive integer T, T <= 100000, denoting the number of test cases. This is followed by each test case per line. 

Each test case consists of a line containing 3 integers a,b and c denoting the sides of a triangle. All of these sides will be between 1 and 100, inclusive. The sides a,b and c can be given in any order. 

출력
For each test case, the output contains a line in the format Case #x: M, where x is the case number (starting from 1) and M is “YES” when the given triangle is a right triangle or “NO” otherwise. Note that the quotes are not required to be outputted. 
"""

for T in range(1, int(input()) + 1):
    lines = list(map(int, input().split()))
    
    c = max(lines)
    lines.remove(max(lines))
    a, b = lines[0], lines[1]
    
    bool_value = None
    if c ** 2 == a ** 2 + b ** 2:
        print(f"Case #{T}: YES")
    else:
        print(f"Case #{T}: NO")