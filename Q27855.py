"""
문제
Cornhole is a popular game in which players take turns throwing bean bags at an angled board with a hole in its far end. The object is to score points by either landing a bag on the board (one point) or getting the bag in the hole (three points).



(https://www.playcornhole.org/pages/rules)

Each player is given four bean bags. Players stand about 30 feet from the board and alternate throwing the bags, on at-a-time, toward the board. After each player has thrown their four bags, cancellation scoring is performed. That is, each player tally’s up their score (three points for each of their bags that went through the hole, and one point for each of their bags that’s on the board). If player 1 has more points than player 2, player one scores the difference in points. If player 2 has more points than player 1, player 2 scores the difference in points. If both players have the same number of points, then neither player scores any points. As an example, suppose that player 1 had two bags go through the hole and one bag on the board and player 2 had four bags on the board. The result is that player 1 would score three points for that round.

For this problem, you will be given the number of bags that each player had go through the hole and the number of bags that stayed on the board. You will calculate who (if anyone) scores any points using cancellation scoring for the round and if so, how many.

입력
Input consists of two lines. The first line of input contains two space separated non-negative integers H1 and B1, where H1 is the number of bags player 1 got through the hole and B1 is the number of bags player 1 got on the board (0 ≤ H1 + B1 ≤ 4). The second line of input contains two space separated decimal integers H2 and B2, where H2 is the number of bags player 2 got through the hole and B2 is the number of bags player 2 got on the board (0≤ H2 + B2 ≤ 4).

출력
There is a single line of output. If no one scores any points, the output is the string NO SCORE, otherwise, the line contains two space separated decimal integers P and N, where P is the player number (1 or 2) and N is the number of points the player scored (1 ≤ N ≤ 12).

"""
total_score = []
for i in range(2):
    H, B = map(int, input().split())
    
    total_score.append(H * 3 - (4 - B))

# if total_score[0] > total_score[1]:
#     print()
if total_score[0] == total_score[1]:
    print("NO SCORE")
else:
    print(total_score.index(max(total_score)) + 1, max(total_score) - min(total_score))