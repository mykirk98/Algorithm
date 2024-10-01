"""
문제
Whenever somebody goes to an ATM to withdraw or deposit money, a calculation has to be done to keep the person's bank balance correct. Your task in this problem is to do such calculations. There is a bank rule that says that a customer may not have an overdraft of more than $200, so any withdrawal that would take the balance below –200 must be stopped. (A minus sign is used to indicate an overdraft, or negative balance).

입력
Input consists of a number of lines, each representing a transaction. Each transaction consists of an integer representing the starting balance (between –200 and +10,000), the letter W or the letter D (Withdrawal or Deposit), followed by a second integer representing the amount to be withdrawn or deposited (between 5 and 400). Input will be terminated by a line containing 0 W 0.

출력
Output consists of one line for each line of input showing the new balance for each valid transaction If a withdrawal would take the balance below -200, the output must be the words ‘Not allowed’.
"""

while True:
    calculation = list(map(str, input().split()))
    calculation[0], calculation[2] = int(calculation[0]), int(calculation[2])
    
    if calculation[0] == 0 and calculation[2] == 0:
        break
    
    if calculation[1] == 'W':
        result = calculation[0] - calculation[2]
    elif calculation[1] == 'D':
        result = calculation[0] + calculation[2]
    
    if result < -200:
        print('Not allowed')
    else:
        print(result)