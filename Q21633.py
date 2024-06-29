"""
문제
Tanya has an account in "Redgotts" bank. The bank has the commission to transfer money to "Bluegotts" bank that her friend Vanya has the account in.

Tanya has read her bank rules and learned the following:

The commission for the bank transfer is 
$25$ tugriks plus 
$1\%$ of the sum transferred. However, the commission is never smaller than 
$100$ tugriks, and cannot exceed 
$2000$ tugriks.

Tanya is planning to transfer 
$k$ tugriks to Vanya. Help her find out what the commission would be.

입력
Input is a single integer 
$k$ (
$200 \le k \le 10^9$).

출력
Output one floating point value: the commission for the transfer. The value must be printed with at least two exact digits after the decimal point.
"""

k = int(input())

transfer = 25 + k * 0.01
if transfer > 2000:
    transfer = 2000
elif transfer < 100:
    transfer = 100
print(f"{transfer:.2f}")