S = input()

a_to_z = 'abcdefghijklmnopqrstuvwxyz'

for i in a_to_z:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')