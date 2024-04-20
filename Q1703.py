"""
문제
branchorama 나무는 특이한 규칙을 가지고 성장합니다. 어린 branchorama 초목은 하나의 잎을 꼭대기에 가진 가는 묘목이며, 그 잎에는 생장점이 있습니다.
성장하는 계절 동안 나무의 생장점들은 여러 개의 가지로 나뉘게 되며, 성장이 끝나면 각 가지는 생장점을 가진 하나의 잎을 꼭대기에 매달게 됩니다. 놀랍게도 같은 나무의 모든 생장점들은 같은 숫자(splitting factor)의 가지로 나뉘며, 그 숫자는 해가 지남에 따라 변합니다.

아래의 예는 Brown 씨의 과수원에서 한 branchorama 나무가 유목에서부터 3년간 자란 결과를 보여줍니다.

예시에서 예측할 수 있듯이, branchorama 나무는 과밀하게 성장하는 경향이 있습니다. 따라서 Brown 씨는 매 겨울마다 과도하게 성장한 나무들의 가지를 쳐냅니다. 아래는 가지를 쳐낸  branchorama 나무의 예입니다
"""
while True:
    List = list(map(int, input().split()))
    if List[0] == 0:
        break
    branch = 1
    for i in range(List[0]):
        branch = branch * List[2*i+1] - List[2*i+2]
    print(branch)