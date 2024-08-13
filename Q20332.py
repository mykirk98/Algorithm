"""
문제
A solid competitive programming team can rack up a lot of prize money. Knowing how strong your team is, you are certain to win a lot of contests, so you had better sit down now and check that everybody will receive the same fair distribution of winnings.

You will participate in multiple contests, and at the end of each one receive a set amount of prize money. You can distribute any amount to each of the three members of your team each time, but by the end everyone must have the same amount of total winnings.

Can you distribute the winnings such that everyone gets an equal amount by the end?

입력
One line containing the number of contests, 
$n$ (
$1 \le n \le 10^4$).
One line containing the prize purse for each contest, 
$w_1 \ldots w_n$ (
$1 \le w \le 10^5$).
출력
Output yes if the winnings can be distributed equally between three contestants, otherwise no.
"""

n = int(input())
warray = list(map(int, input().split()))

if sum(warray) % 3 == 0:
    print('yes')
else:
    print('no')