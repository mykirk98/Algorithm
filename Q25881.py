"""
문제
To encourage customers to conserve energy (and protect the environment), the electric companies typically have a lower rate for the first 1000 kilowatt-hour (KWH) of electric usage and a higher rate for the additional usage (KWH is a derived unit of energy equal to 3.6 megajoules).

Given the rate (per KWH) for the first 1000 KWH usage, the rate (per KWH) for the additional usage, and a customer’s energy consumption, you are to determine the charges (bill) for the customer.

입력
The first input line contains two integers (each between 2 and 20, inclusive), indicating the rate/KWH for the first 1000 KWH and the rate/KWH for the additional usage, respectively. The next input line contains a positive integer, n, indicating the number of customers to process. Each of the following n input lines contains an integer (between 1 and 50000, inclusive), indicating a customer’s energy consumption.

출력
For each customer, print the energy consumption, followed by a space, followed by the charges.
"""

low, high = map(int, input().split())

for n in range(int(input())):
    consumption = int(input())

    if consumption <= 1000:
        cost = low * consumption
    else:
        cost = low * (1000) + high * (consumption - 1000)
    
    print(consumption, cost)