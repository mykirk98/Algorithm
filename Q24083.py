"""
문제
JOI 高校の生徒である葵はアナログ時計を手に入れた．この時計には外周に沿って 12 個の目盛りがあり，時計回りに 1 から 12 までの番号が順に付けられている．

この時計の短針は時計回りに回っており，1 時間で目盛り 1 つ分進む．

たった今，短針がある目盛りを指した．この目盛りの番号は A である．

この状態からちょうど B 時間が経過したときに短針が指す目盛りの番号を出力せよ．

입력
入力は以下の形式で標準入力から与えられる．

A
B
출력
短針が A を指してからちょうど B 時間が経過したときに短針が指す目盛りの番号を出力せよ．
"""

A = int(input())
B = int(input())

print((A + B) % 12 if (A + B) % 12 != 0 else 12)