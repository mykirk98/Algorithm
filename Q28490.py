"""
문제
Stuart has 
$n$ rectangular frames, which are numbered from 
$1$ to 
$n$. Frame 
$i$ is a rectangle with height 
$h[i]$ and width 
$w[i]$.

The size of a frame is the area that it covers. Stuart wants you to help him find the area covered by the largest size frame that he has.

입력
The first line of input contains exactly 
$1$ integer, 
$n$.

The next 
$n$ lines of input contains two space-separated integers each. The 
$i$-th such line of input will contain 
$h[i]$ and 
$w[i]$ respectively, representing the height and width of frame 
$i$.

출력
The output should contain one integer, the area covered by the largest size frame Stuart has.
"""
maximum = 0
for n in range(int(input())):
    h, w = map(int, input().split())
    maximum = max(maximum, w * h)

print(maximum)