H, M = map(int, input().split())

if H > 0:
    if 0 <= M < 45:
        H -= 1
        M += 15

    else:
        M -= 45

elif H == 0:
    if 0 <= M < 45:
        H += 23
        M += 15
    else:
        M -= 45
        
print(f"{H} {M}")