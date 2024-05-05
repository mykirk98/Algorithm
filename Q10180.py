"""
문제
When Starfleet headquarters gets a request for an exploration expedition, they need to determine which ship from those currently docked in the docking bay to send. They decide to send whichever ship is currently able to make the expedition based on how much fuel is currently stored on the ship as well as how long it will take the ship to arrive at the expected destination. Due to the age and current maintenance of the ships, each ship travels at a different top speed and has a different fuel consumption rate. Each ship reaches its top speed instantaneously.

입력
Input begins with a line with one integer T (1 ≤ T ≤ 50) denoting the number of test cases. Each test case begins with a line with two space-separated integers N and D, where N (1 ≤ N ≤ 100) denotes the number of ships in the docking bay and D (1 ≤ D ≤ 106) denotes the distance in light-years to the expedition site. Next follow N lines with three space-separated integers vi, fi, and ci, where vi (1 ≤ vi ≤ 1000) denotes the top speed of ship i in light-years per hour, fi (1 ≤ fi ≤ 1000) denotes the fuel on ship i in kilos of deuterium, and ci (1 ≤ ci ≤ 1000) denotes the fuel consumption of ship i in kilos of deuterium per hour.

출력
For each test case, print a single integer on its own line denoting the number of ships capable of reaching the expedition site. Be careful with integer division!
"""

for T in range(int(input())):
    N, D = map(int, input().split())
    counter = 0
    for n in range(N):
        vi, fi, ci = map(int, input().split())
        
        if vi * fi / ci >= D:
            counter += 1
    
    print(counter)