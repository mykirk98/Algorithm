"""
문제
Your friend has secretly picked 
$N$ consecutive positive integers between 
$1$ and 
$100$, and wants you to guess if their sum is even or odd.

If the sum must be even, output 'Even'.  If the sum must be odd, output 'Odd'.  If the sum could be even or could be odd, output 'Either'.

입력
The input is a single integer 
$N$ with 
$1 \le N \le 10$.

출력
Output a single word. The word should be 'Even', 'Odd', or 'Either', according to the rules given earlier.
"""

N = int(input())

if N % 4 == 0:
    print('Even')
elif N % 2 == 0:
    print('Odd')
else:
    print('Either')