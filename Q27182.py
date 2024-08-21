"""
문제
Petya lives in Saint Petersburg and he is keen on meteorology. It is widely believed that it constantly rains in Saint Petersburg. Petya has decided to statistically prove or disprove this statement. For this Petya started a rain diary and every week at Sunday he makes a record, whether it is rainy or not. Petya signs every record with a number of current day in a month, days in a month are numerated from 1 to number of days in the current month (from 28 to 31 in a different monthes).

Today Petya opened his diary and realized, that he made the last record two weeks ago and forgot to make a record last Sunday. Petya remembers, that there was a heavy rain a week ago. He decided to make two records: for today and for the last Sunday. He knows the number of the current day 
$n$ and sees the number 
$m$ in the two weeks ago record. What is the number Petya should sign his record for the last Sunday?

입력
The first line of the input contains two integers 
$n$ and 
$m$ (
$1 \le n, m \le 31$) --- the number of the current day of the month and the number that the record was signed two weeks ago.

출력
Output a single number -- what number should the record be signed for the last Sunday.
"""

n, m = map(int, input().split())

if n - 7 > 0:
    print(n-7)
else:
    print(m+7)