"""
문제
1 個 A 円の飴を B 個と，C 円の袋を 1 つ買う．合計金額はいくらか求めよ．

입력
入力は以下の形式で与えられる．

A
B
C
출력
合計金額を，単位 (円) を省いて出力せよ．

答え以外は何も出力しないこと．(入力を促す文章なども出力しないこと．)
"""

A = int(input())
B = int(input())
C = int(input())

print(A * B + C)