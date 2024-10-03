"""
문제
UCPC 초등학교의 체육 시간이 다가왔습니다. 체육 선생님이 학교에 나오지 못해 체육 시간을 대신 맡게 된 수학 선생님 키파는, 이제는 해져서 축구공처럼 보이지도 않는 공을 던져 주고 축구든 피구든 하라고 한 뒤, 공을 갖고 재밌게 노는 아이들을 운동장 구석에서 지켜보며 자신이 초등학생이던 시절의 체육 시간을 떠올렸습니다.

초등학생의 키파는 몸이 약했습니다. 축구도 몇십 초 이상 뛰는 게 힘들어서, 피구도 공이 몸에 맞으면 다음 날 몸이 너무 아파서, 언제나 운동장 구석에 앉아 재밌게 노는 친구들을 바라만 보았습니다. 그러다 심심해지면 운동장 위에 낙서를 했습니다. 지금 아이들을 바라보고 있자니 문득 그때의 자신이 떠올랐습니다. 이제 생각해 보면 그런 생각의 시간이 있었기에 수학이 재밌어진 것이 아닐까 싶기도 합니다. 어느새 키파는 자신도 모르게 초등학생 때처럼 운동장 위에 나뭇가지로 원을 그리고 있었습니다.

초등학교 운동장에 앉아 있었을 때에는 커다란 원을 그리고 싶었습니다. 어린 키파의 눈에도 원은, 구불구불하지만 질서 있는 듯, 동그랗다는 느낌이 참 마음에 들었나 봅니다. 운동장이 모두 내 것이 된 것처럼 그저 이곳을 뛰어다니고만 싶어졌습니다. 뛰어다니며 원을 그리고 싶었습니다. 하지만 체육 선생님이 아니라 수학 선생님이 된 키파는, 뛰어다니기에는 여전히 몸이 그리 좋지 않았습니다. 운동장이 칠판이라고 생각하며 운동장 비슷한 직사각형을 그리고, 그 안에 꽉 찬 원을 그릴 수밖에 없었습니다.

여러분이 대신 키파의 꿈을 이루어 줍시다. 직사각형 모양의 운동장이 주어지면 운동장 안에서 그릴 수 있는 가장 커다란 원을 그려 줍시다. 그러고 나서 키파에게 원의 반지름의 길이가 얼마인지 알려 줍시다.

입력
첫 줄에 운동장의 한 변의 길이 H가 미터(m) 단위로 주어집니다. (5 ≤ H ≤ 1 000)

둘째 줄에 운동장의 다른 한 변의 길이 W가 미터(m) 단위로 주어집니다. (5 ≤ W ≤ 1 000)

입력으로 들어오는 모든 수는 정수입니다.

출력
첫 줄에 운동장 안에 그릴 수 있는 가장 큰 원의 반지름의 길이를 센티미터(cm) 단위로 출력합니다. 입력 조건 하에서 이 값은 정수임을 보일 수 있으므로, 정수 형태로 출력합니다.
"""

H = int(input())
W = int(input())

diameter = min(H, W)

radius = diameter / 2 * 100

print(int(radius))