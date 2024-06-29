"""
문제
2 つの整数 A, B が与えられる．A+B, A-B の中で最大の値と最小の値を順に出力せよ．

입력
入力は以下の形式で標準入力から与えられる．

A B
출력
出力は 2 行からなる．

1 行目に，A+B, A-B の中で最大の値を出力せよ．

2 行目に，A+B, A-B の中で最小の値を出力せよ．
"""

A, B = map(int, input().split())

max_num = max(A + B, A - B)
min_num = min(A + B, A - B)

print(max_num)
print(min_num)