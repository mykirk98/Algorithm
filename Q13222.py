"""
문제
Young Sean threw matches all over the floor of his room.

His mum did not like that and ordered him to put all the matches in a box.
Sean soon noticed that not all of the matches on the floor fit in the box,
so he decided to take the matches that don't fit and throw them in the neighbour's garbage, where his mum (hopefully) won't find them.

Help Sean determine which of the matches fit in the box his mom gave him.
A match fits in the box if its entire length can lie on the bottom of the box.
Sean examines the matches one by one.

입력
The first line of input contains an integer N (1 ≤ N ≤ 50), the number of matches on the floor, and two integers W and H, the dimensions of the box (1 ≤ W ≤ 100, 1 ≤ H ≤ 100).

Each of the following N lines contains a single integer between 1 and 1000 (inclusive), the length of one match.

출력
For each match, in the order they were given in the input, output on a separate line "YES" if the match fits in the box or "NO" if it does not.
"""

N, W, H = map(int, input().split())

diagonal = (W ** 2 + H ** 2) ** 0.5
for n in range(N):
    print("YES" if int(input()) <= diagonal else "NO")