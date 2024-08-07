"""
문제
JOI アイスクリーム店は，非常に高さのあるアイスクリームタワーが名物のアイスクリーム店である．アイスクリームタワーとは，ベースとなるアイスクリームの上に，追加のアイスクリームを 0 個以上積み重ねたものである．

ベースとなるアイスクリームの金額は 250 円で，高さは A cm である．追加のアイスクリームは 1 個につき 100 円で，1 個追加するごとにアイスクリームタワーの高さが B cm 増える．

あなたは，この店で高さが S cm 以上のアイスクリームタワーを買いたい．高さが S cm 以上のアイスクリームタワーを買うために必要な金額の最小値を求めよ．

입력
入力は以下の形式で標準入力から与えられる．

S
A
B
출력
高さ S cm 以上のアイスクリームタワーを買うために必要な金額の最小値を，単位 (円) を省いて出力せよ．
"""

from math import ceil

S = int(input())
A = int(input())
B = int(input())

if S - A <= 0:
    print(250)
else:
    icecream = ceil((S - A) / B)
    print(250 + icecream * 100)