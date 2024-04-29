"""
문제
In Emily’s country it is estimated that a person dies every 7 seconds, and a person is born every 4 seconds. Given a beginning population, estimate the population after a certain period of time.

입력
The first line of input will contain a single integer n that indicates the number of lines to follow. Each line will consist of two integers, p and t, where p is the beginning population, and t is the amount of time that will pass. Both p and t will be between the number 1 and 2,000,000,000.

출력
Output the estimated population after the period of time based on the above statistics.
"""

for n in range(int(input())):
    p, t = map(int, input().split())
    
    print(p - t // 7 + t // 4)