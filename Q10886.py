"""0 = not cute / 1 = cute"""
N = int(input())
agree, disagree = 0, 0

for n in range(N):
    n = int(input())
    
    if n == 0:
        disagree += 1
    elif n == 1:
        agree += 1
    else:
        pass

if agree > disagree:
    print("Junhee is cute!")
elif agree < disagree:
    print("Junhee is not cute!")
else:
    pass