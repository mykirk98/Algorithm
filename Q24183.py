c4, a3, a4 = map(int, input().split())

C4 = c4 * 0.229 * 0.324
A3 = a3 * 0.297 * 0.420
A4 = a4 * 0.210 * 0.297

print(C4 + A3 + A4)