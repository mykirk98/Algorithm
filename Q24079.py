"""
문제
A 地点から B 地点に移動するのに X 時間，B 地点から C 地点に移動するのに Y 時間かかる．

A 地点から B 地点を経由して C 地点に移動するとき，Z 時間 30 分以内に移動することができるか判定せよ．

입력
入力は以下の形式で標準入力から与えられる．

X
Y
Z
출력
Z 時間 30 分以内に移動することができるならば 1 を，そうでない場合は 0 を出力せよ．
"""

X = int(input())
Y = int(input())
Z = int(input())

print(1 if X + Y <= Z else 0)