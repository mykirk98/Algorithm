"""
문제
2 つの整数 A, B が与えられる．

2022 年 11 月 A 日の B 週間後の日が 2022 年 11 月ならば 1 を，2022 年 11 月でないならば 0 を出力せよ．

ただし，2022 年 11 月は 2022 年 11 月 1 日から 2022 年 11 月 30 日までの 30 日間であり，x 週間後の日とは (7 × x) 日後の日のことを指す．

입력
入力は以下の形式で与えられる．

A
B
출력
2022 年 11 月 A 日の B 週間後の日が 2022 年 11 月ならば 1 を，2022 年 11 月でないならば 0 を出力せよ．
"""

A = int(input())
B = int(input())

print(1 if A + 7 * B <= 30 else 0)