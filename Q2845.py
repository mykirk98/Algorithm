"""파티가 끝나고 난 뒤"""
L, M = map(int, input().split())
total = L * M
List = [0, 0, 0, 0, 0]
List[0], List[1], List[2], List[3], List[4] = map(int, input().split())

difference = []
for l in List:
    difference.append(l - total)

print(*difference)