"""
문제
Your animals have begun producing products, and you’re honestly a little strapped for cash. Since you have far more animal byproducts than you know what to do with, you’ve decided to begin shipping them for extra money. Given the information in your shipping ledger, determine how much money you can expect to make.

입력
The first line will contain a single integer n that indicates the number of data sets that follow. Each data set will start with a single integer x denoting how many items follow. The next x lines consist of a string, and integer, and a floating point number to two decimal places, representing the name of what was sold, the quantity, and the unit price of each item.

출력
For each test case, output the amount of money you expect to make with all of the goods you sold, rounded to two decimal places.
"""

for n in range(int(input())):
    total = 0
    for x in range(int(input())):
        name, quantity, price = map(str, input().split())
        quantity, price = int(quantity), float(price)
        total += quantity * price
    print(f"${total:.2f}")