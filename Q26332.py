"""
문제
To encourage customers to shop more, some stores charge lower prices if you buy multiples of an item. For example, if you buy one, it may cost you $5 but if you buy two, it will cost you $8 instead of $10.

Let’s assume a store provides discounts as follows:

No discount if you buy only one.
$2 discount for each additional item if you buy more than one.
Given the number of items a customer has purchased and the price for one item, you are to compute the total cost for the customer.

입력
The first input line contains a positive integer, n, indicating the number of customers to check. The customers are on the following n input lines, one customer per line. Each line provides two integers; the first integer c (1 ≤ c ≤ 100) is the number of items purchased by the customer, and the second integer p (3 ≤ p ≤ 50) is the price for one item.

출력
For each customer, print two lines of output. The first line will contain the two input values separated by a single space. The second output line will contain the total cost for the customer. There should be no leading or trailing spaces on any output line.
"""

for n in range(int(input())):
    c, p = map(int, input().split())

    total = 0
    if c == 1:
        total = c * p
    else:
        total = 1 * p + (c - 1) * (p - 2)
    print(c, p)
    print(total)