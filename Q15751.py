"""
문제
One of the farming chores Farmer John dislikes the most is hauling around lots of cow manure. In order to streamline this process, he comes up with a brilliant invention: the manure teleporter! Instead of hauling manure between two points in a cart behind his tractor, he can use the manure teleporter to instantly transport manure from one location to another.

Farmer John's farm is built along a single long straight road, so any location on his farm can be described simply using its position along this road (effectively a point on the number line). A teleporter is described by two numbers 
$x$ and 
$y$, where manure brought to location 
$x$ can be instantly transported to location 
$y$, or vice versa.

Farmer John wants to transport manure from location 
$a$ to location 
$b$, and he has built a teleporter that might be helpful during this process (of course, he doesn't need to use the teleporter if it doesn't help). Please help him determine the minimum amount of total distance he needs to haul the manure using his tractor.

입력
The first and only line of input contains four space-separated integers: 
$a$ and 
$b$, describing the start and end locations, followed by 
$x$ and 
$y$, describing the teleporter. All positions are integers in the range 
$0 \ldots 100$, and they are not necessarily distinct from each-other.

출력
Print a single integer giving the minimum distance Farmer John needs to haul manure in his tractor.
"""

a, b, x, y = map(int, input().split())

a, b = min(a, b), max(a, b)
x, y = min(x, y), max(x, y)

if b - a < abs(x - a) + abs(y - b):
    print(b - a)
else:
    print(abs(x - a) + abs(y - b))