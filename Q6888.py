"""
문제
In CS City, a mathematical place to live, the mayor is elected every 4 years, the treasurer is appointed every 2 years, the chief programmer is elected every 3 years and the dog-catcher is replaced every 5 years.

This year, Year 
$X$, the newly elected mayor announced the appointment of the new treasurer, a new dog-catcher and congratulated the chief programmer for winning the recent election. That is, all positions were changed over. This is highly unusual. You will quantify how unusual this really is.

Write a program that inputs the year 
$X$ and the future year 
$Y$ and lists all years between 
$X$ and 
$Y$ inclusive when all positions change.
"""

X = int(input())
Y = int(input())

year = X
while year <= Y:
    print(f"All positions change in year {year}")
    year += 60