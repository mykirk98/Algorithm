"""
문제
After a long time at home during the quarantine, in November you decided to go to work by bicycle! Since you do not have your own bicycle, you have to rent one. The bike rental allows you to choose one of two monthly options:

The monthly fee is 
$a$ roubles. Every day, the first 
$30$ minutes are free, and every minute above that costs 
$x$ roubles.
The monthly fee is 
$b$ roubles. Every day, the first 
$45$ minutes are free, and every minute above that costs 
$y$ roubles.
There are 
$21$ working days in November, and you spend 
$T$ minutes commuting to work and back home in total every day. Calculate how many roubles you would spend if you use either one of two monthly options.

입력
The first four lines of the input contain integers 
$a$, 
$x$, 
$b$, and 
$y$ (
$0 \leq a, x, b, y \leq 100$), each on a separate line. The last line contains a single integer 
$T$ (
$1 \leq T \leq 1440$) --- the total time spent on a bicycle during each day.

출력
The only line of the output should contain two integers --- the amount of money you would spend on the first option and the second option, respectively.
"""

a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

first_option = a + 21 * (T - 30 if T - 30 > 0 else 0) * x

second_option = b + 21 * (T - 45 if T - 45 > 0 else 0) * y

print(first_option, second_option)