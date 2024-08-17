"""
문제
You are organizing a marathon with N runners. Every runner is given a distinct number from 1 to N, so they can be easily identified.

You record the number of each runner as they cross the finish line. Unfortunately, you notice that only N − 1 runners have finished. Which runner is still out there?

입력
The first line of input contains the integer N (1 ≤ N ≤ 215). The next line contains N −1 distinct integers in the range from 1 to N, representing the numbers of runners who have crossed the finish line.

출력
Output the number of the runner who has not crossed the finish line.
"""

runners = list(range(1, int(input())+1))
finished = list(map(int, input().split()))

for f in finished:
    runners.remove(f)

print(*runners)