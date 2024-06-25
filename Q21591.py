"""
문제
Your school has provided you with a laptop computer! However, they insist on putting a laptop sticker with their logo on your new computer. That sticker might be very large, and it can’t be rotated! Will it fit, with one centimeter to spare on all sides?

입력
The single line of input contains four integers 
$w_c$, 
$h_c$, 
$w_s$ and 
$h_s$ (
$1 \le w_c, h_c, w_s, h_s \le 1,000$), where 
$w_c$ is the width of your new laptop computer, 
$h_c$ is the height of your new laptop computer, 
$w_s$ is the width of the laptop sticker, and 
$h_s$ is the height of the laptop sticker. All measurements are in centimeters.

출력
Output a single integer, which is 1 if the laptop sticker will fit on your new laptop computer, without rotating, but with one centimeter space on all sides, and 0 if the laptop sticker won’t fit.
"""

wc, hc, ws, hs = map(int, input().split())

if wc - ws >= 2 and hc - hs >= 2:
    print(1)
else:
    print(0)