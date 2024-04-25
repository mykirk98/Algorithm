"""
문제
A volcano has recently erupted in Geldingadalur, Iceland. Fortunately this eruption is relatively small, and---unlike the infamous Eyjafjallajökull eruption---is not expected to cause delayed international flights or global outrage.

There is some concern about the magmatic gas that has been released as part of the eruption, as it could pose danger to human populations in the surrounding area. Scientists have estimated the total amount of gas emitted, which, due to lack of wind, has spread out uniformly across a circular area around the centre of the volcano. The authorities have evacuated the area, and would now like to close it off by surrounding the perimeter with barrier tape.

입력
The input consists of:

One line with an integer 
$a$ (
$1 \le a \le 10^{18}$), the total area covered by gas in square metres.
출력
Output the total length of barrier tape needed to surround the area covered by gas, in metres. Your answer should have an absolute or relative error of at most 
$10^{-6}$.
"""

from math import pi

a = int(input())

r = (a / pi) ** 0.5

length = 2 * pi * r

print(length)