"""
문제
JOI 君は情報の試験を 3 回受けた．試験の点数はすべて 0 以上 100 以下の整数である．

JOI 君の成績は 3 回の試験の点数のうち高い方から 2 つを足し合わせた合計によって決まる．

3 回の試験の点数 A, B, C が与えられたとき，3 回の試験の点数のうち高い方から 2 つを足し合わせた合計を出力するプログラムを作成せよ．

입력
入力は以下の形式で標準入力から与えられる．

A B C
출력
3 回の試験の点数のうち高い方から 2 つを足し合わせた合計を 1 行で出力せよ．
"""

score = list(map(int, input().split()))

score.remove(min(score))
print(sum(score))