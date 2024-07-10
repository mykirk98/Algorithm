"""
문제
The amount of income tax imposed on any taxpayer depends on his/her income. For an income less than or equal to 1,000,000 Oshloobs, no tax is paid. For an income greater than 1,000,000 and less than or equal to 5,000,000 Oshloobs, the tax is 10% of the income. For an income over 5,000,000 Oshloobs, the tax is 20% of the income. You should write a program to calculate the net income of any given employee after the deducted tax.

입력
There are multiple lines in the input. Each line contains an employee’s income before the tax, which is a positive integer, a multiple of 1000, and not greater than 10,000,000. The input terminates with a line containing 0 which should not be processed.

출력
For each employee, output a line containing the net income after the deducted tax.
"""

while True:
    income = int(input())
    if income == 0:
        break

    if income <= 1000000:
        tax = 0
    elif 1000000 < income <= 5000000:
        tax = 0.1
    else:
        tax = 0.2
    
    after_taxed = income * (1 - tax)
    print(int(after_taxed))