"""
문제
Travis was recently saddled with writing the easy problem for a competitive programming contest aimed at high school students. Writing an easy problem is a bit of a challenge for Travis; a problem labeled as “Medium Difficulty Level” by Travis typically ends up being the hardest problem of the set!

But this time things were different. When the contest was over, Travis was happy that everyone solved his problem. However, some of the other judges informed Travis a problem is easy only if at least half of the contestants solve the problem in the first half of the contest.

Travis has some data on his problem, and now he wants to determine: was his problem truly easy?

In programming competitions, the term “solves” is used to refer to the number of correct submissions for a problem, i.e., that many contestants solved the problem.

Given the number of solves for Travis’s problem at the end of the first half and at the end of the contest, determine whether at least half the people solved the problem in the first half. Note that solves at the end of the contest includes solves of the first half as well.

입력
There is only one input line; it contains two integers, s1 and s2 (0 ≤ s1 ≤ s2; 1 ≤ s2 ≤ 100), representing solves of Travis’s problem at the end of the first half and at the end of the contest, respectively.

출력
Print “E” (quotes for clarity) if the problem is considered easy by the other judges’ standards. Print “H” (quotes for clarity) if the problem is not considered easy by the other judges’ standards. Everyone knows that if Travis is not writing an easy problem, the problem is probably hard!

"""

s1, s2 = map(int, input().split())

if s1 / s2 >= 0.5:
    print('E')
else:
    print('H')