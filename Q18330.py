"""
문제
The government of Neverland has recently announced a new petrol rationing plan with an unexpected price hike. According to the new plan, each person receives a quota of 60 liters per month in a fuel card. Each liter of petrol costs 1500 Oshloobs if it is within quota. Any extra fueling costs 3000 Oshloobs per liter.

After recovering from the shock, Mahya is trying to figure out how dark is the future. The current month is coming to an end, and Mahya has some quota left in her fuel card, remaining available for the next month. A quota of 60 liters will also be added to her fuel card just at the beginning of the next month. She also has a prediction of the amount of petrol that will be used in the next month. She now wants to know how much she should pay for petrol in the next month. However, she is too lazy to do that on her own. So, she needs your help to calculate the cost for her. 

입력
The input consists of two lines. The first line contains an integer n (0 ⩽ n ⩽ 200), specifying the amount of petrol that will be used in the next month. The second line contains an integer k (0 ⩽ k ⩽ 360), showing the quota left in Mahya’s fuel card at the end of current month.

출력
Print the amount of money (in Oshloobs) that Mahya will pay for petrol in the next month.
"""

n = int(input())
k = int(input())

x = min(k + 60, n)

result = x * 1500 + (n - x) * 3000

print(result)