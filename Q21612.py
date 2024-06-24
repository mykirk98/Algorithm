"""
문제
At sea level, atmospheric pressure is 100 kPa and water begins to boil at 100◦C. As you go above sea level, atmospheric pressure decreases, and water boils at lower temperatures. As you go below sea level, atmospheric pressure increases, and water boils at higher temperatures. A formula relating atmospheric pressure to the temperature at which water begins to boil is

P = 5 × B − 400

where P is atmospheric pressure measured in kPa, and B is the temperature at which water begins to boil measured in ◦C.

Given the temperature at which water begins to boil, determine atmospheric pressure. Also determine if you are below sea level, at sea level, or above sea level.

Note that the science of this problem is generally correct but the values of 100◦C and 100 kPa are approximate and the formula is a simplification of the exact relationship between water’s boiling point and atmospheric pressure.

입력
The input is one line containing an integer B where B ≥ 80 and B ≤ 200. This represents the temperature in ◦C at which water begins to boil.

출력
The output is two lines. The first line must contain an integer which is atmospheric pressure measured in kPa. The second line must contain the integer -1, 0, or 1. This integer represents whether you are below sea level, at sea level, or above sea level, respectively.
"""

B = int(input())

P = 5 * B - 400

print(P)

if P < 100:
    print(1)
elif P == 100:
    print(0)
else:
    print(-1)