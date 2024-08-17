"""
문제
The movie “Magnificent 7” has become a western classic. Well, this year we have 10 coaches training the UCF programming teams and once you meet them, you’ll realize why they are called the “Majestic 10”! The number 10 is actually special in many different ways. For example, in basketball, they keep track of various statistics (points scored, rebounds, etc.) and if a player has 10+ (10 or more) in a particular stat, they call it a double.

Given three stats for a basketball player, you are to determine how many doubles the player has, i.e., how many of the stats are greater than or equal to 10.

입력
The first input line contains a positive integer, n, indicating the number of players. Each of the following n input lines contains three integers (separated by a space and each between 0 and 100, inclusive), providing the three stats for a player.

출력
Print each input line as it appears in the input. Then, on the following output line, print a message indicating how many stats are greater than or equal to 10:

print zilch if none of the three stats is greater than or equal to 10,
print double if one of the three stats is greater than or equal to 10,
print double-double if two of the three stats are greater than or equal to 10,
print triple-double if all three stats are greater than or equal to 10.
Leave a blank line after the output for each player.
"""

for n in range(int(input())):
    stats = list(map(int, input().split()))
    
    count = 0
    for stat in stats:
        if stat >= 10:
            count += 1
    
    print(*stats)
    if count == 3:
        print('triple-double')
    elif count == 2:
        print('double-double')
    elif count == 1:
        print('double')
    elif count == 0:
        print('zilch')
    else:
        pass
    
    print()