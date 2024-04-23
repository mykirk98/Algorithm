"""
문제
2 つの整数 A, B が与えられる．

A と B の大小を比較し，A ＜ B ならば -1 を，A ＝ B ならば 0 を，A ＞ B ならば 1 を出力せよ．

입력
入力は以下の形式で標準入力から与えられる．

A
B
출력
A ＜ B ならば -1 を，A ＝ B ならば 0 を，A ＞ B ならば 1 を出力せよ．
"""

A = int(input())
B = int(input())

if A < B:
    print(-1)
elif A == B:
    print(0)
else:
    print(1)