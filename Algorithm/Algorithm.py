def q1000():
    A, B = input().split()
    print(int(A) + int(B))

def q1001():
    A, B = input().split()
    print(int(A) - int(B))

def q10998():
    A, B = input().split()
    print(int(A) * int(B))

def q1002():
    import math

    T = int(input())

    for t in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # 규현과 승환 사이의 거리

        if distance == 0 and r1 == r2:  # 두 원의 중심이 같고 r1과 r2가 같을 때
            print(-1)
        elif distance == (r1 + r2) or distance == abs(r1 - r2):  # 외접원 or 내접원 일 때
            print(1)
        elif abs(r1 - r2) < distance < (r1 + r2):  # 원 두개가 만나서 점 2개일 때
            print(2)
        else:
            print(0)

def q10869():
    # 문제 : 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
    # 입력 : 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
    # 출력 : 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

    A, B = input().split()

    A = int(A)
    B = int(B)

    print(A + B, A - B, A * B, A // B, A % B, sep='\n')

def q10718():
    for i in range(2):
        print('강한친구 대한육군')

def q1008():
    A, B = input().split()
    A, B = int(A), int(B)

    print(A / B)

def q9468():
    score = int(input('score :'))

    if 90 <= score <= 100:
        print('A')
    elif 80 <= score <= 89:
        print('B')
    elif 70 <= score <= 79:
        print('C')
    elif 60 <= score <= 69:
        print('D')
    else:
        print('F')

def q18108():
    print(int(input()) - 543)

def q10430():
    A, B, C = input().split()
    A, B, C = int(A), int(B), int(C)

    print((A + B) % C, ((A % C) + (B % C)) % C, (A * B) % C, ((A % C) * (B % C)) % C, sep='\n')

def q2588():
    A, B = input().split()

    A = int(A)
    B = int(B)

    print(A * (B % 10))
    print(A * (B % 100 // 10))
    print(A * (B // 100))
    print(A * B)

def q11382():
    A, B, C = map(int, input().split())

    print(A + B + C)

def q10171():
    print("\    /\\")
    print(" )  ( ')")
    print("(  /  )")
    print(" \(__)|")

def q10172():
    print("|\_/|")
    print("|q p|   /}")
    print("( 0 )\"\"\"\\")
    print("|\"^\"`    |")
    print("||_/=\\\\__|")

def q1330():
    A, B = map(int, input().split())

    if A > B:
        print(">")
    elif A < B:
        print("<")
    else:
        print("==")

def q2753():
    year = int(input())

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("1")
    else:
        print("0")

def q14681():
    x = int(input())

    y = int(input())

    if x > 0:
        if y > 0:
            print("1")
        else:
            print("4")
    else:
        if y > 0:
            print("2")
        else:
            print("3")

def q2884():
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

def q2525():
    A, B = map(int, input().split())
    C = int(input())

    if (A + ((B + C) // 60)) >= 24:
        A = (A + ((B + C) // 60)) - 24

    else:
        A += (B + C) // 60

    B = (B + C) % 60

    print(f"{A} {B}")

def q2480():
    A, B, C = map(int, input().split())

    if A == B == C:
        print(10000 + A * 1000)
    elif A == B != C:
        print(1000 + A * 100)
    elif B == C != A:
        print(1000 + B * 100)
    elif C == A != B:
        print(1000 + C * 100)
    else:
        print(max(A, B, C) * 100)

def q2739():
    N = int(input())

    for i in range(1, 10):
        print(f"{N} * {i} = {N * i}")

def q10950():
    T = int(input())

    for t in range(T):
        A, B = map(int, input().split())
        print(A + B)

def q8393():
    N = int(input())
    sum = 0

    for n in range(1, N+1):
        sum += n

    print(sum)

def q25304():
    X = int(input())

    N = int(input())

    total_cost = 0
    for n in range(N):
        a, b = map(int, input().split())
    
        total_cost += a * b

    if X == total_cost:
        print('Yes')
    else:
        print('No')

def q25314():
    N = int(input())

    for n in range(N//4):
        print("long", end=' ')

    print('int')
                # print("long " * (N//4) + "int", sep = ' ') 로 한줄로 줄일 수  있다.

def q15552():
    import sys

    T = int(sys.stdin.readline())

    for t in range(T):
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)

def q11021():
    T = int(input())

    for t in range(1, T+1):
        A, B = map(int, input().split())
        print(f'Case #{t}: {A+B}')

def q11022():
    T = int(input())

    for t in range(1, T+1):
        A, B = map(int, input().split())
        print(f'Case #{t}: {A} + {B} = {A+B}')

def q2438():
    N = int(input())

    for n in range(1, N+1):
        print("*" * n)

def q2439():
    N = int(input())

    for n in range(1, N+1):
        print(" "* (N - n) + "*" * n)

def q10952():
    while(1):
        A, B, = map(int, input().split())
        if A == 0 and B == 0:
            break
        else:
            print(A + B)

def q10951():
    while 1:
        try:
            A, B, = map(int, input().split())
            print(A + B)
        except:
            break

def q10807():
    N = int(input())

    list_ex = list(map(int, input().split()))

    v = int(input())

    print(list_ex.count(v))

def q10871():
    N, X = map(int, input().split())

    A = list(map(int, input().split()))

    for n in range(N):
        if X > A[n]:
            print(A[n], end=' ')

def q10818():
    N = int(input())

    A = list(map(int, input().split()))

    print(min(A), max(A))

def q2562():
    L = []

    for i in range(9):
        N = int(input())
        L.append(N)

    print(max(L), L.index(max(L))+1, sep='\n')

def q10810():
    N, M = map(int, input().split())

    basket = [0 for n in range(N)]

    for m in range(M):
        i, j, k = map(int, input().split())

        for a in range(j-i+1):
            basket[i-1+a] = k

    for i in range(N):
        print(basket[i], end=' ')

def q10813():
    N, M = map(int, input().split())

    basket = [i for i in range(1, N+1)]

    for i in range(M):
        i, j = map(int, input().split())

        p = basket[i-1]
        basket[i-1] = basket[j-1]
        basket[j-1] = p

    for n in range(N):
        print(basket[n], end=' ')

def q5597():
    students = [i+1 for i in range(30)]

    for i in range(28):
        attendance = int(input())
        students.remove(attendance)

    result = " ".join(map(str, students))
    print(result)

def q3052():
    List = []

    for i in range(10):
        number = int(input())

        if number%42 not in List:
            List.append(number%42)
        else:
            pass

    print(len(List))

def q10811():
    from math import ceil

    N, M = map(int, input().split())
    basket = [n for n in range(1, N+1)]

    for m in range(M):
        i, j = map(int, input().split())

        for k in range(ceil(abs(j-i)/2)):
            temp = basket[i-1+k]
            basket[i-1+k] = basket[j-1-k]
            basket[j-1-k] = temp

    result = ' '.join(map(str, basket))
    print(result)

def q1546():
    N = int(input())

    scores = list(map(int, input().split()))
    M = max(scores)

    scores_2 = []
    for s in scores:
        scores_2.append(s / M * 100)

    average = sum(scores_2) / N

    print(average)

def q27866():
    S = str(input())

    i = int(input())

    print(S[i-1])

def q2743():
    S = input()

    print(len(S))

def q9086():
    T = int(input())

    for t in range(T):
        S = input()
        print(S[0] + S[-1])

def q11654():
    a = input()

    print(ord(a))

def q11720():
    N = int(input())

    input_number = input()

    sum = 0
    for n in range(N):
        sum += int(input_number[n])

    print(sum)

def q10809():
    S = input()

    a_to_z = 'abcdefghijklmnopqrstuvwxyz'

    for i in a_to_z:
        if i in S:
            print(S.index(i), end=' ')
        else:
            print(-1, end=' ')

def q2675():
    T = int(input())

    for t in range(T):
        R, S = map(str, input().split())
        R = int(R)

        for s in S:
            print(s * R, end='')
        print()

def q1152():
    S = input().split()

    print(len(S))

def q2908():
    A, B = map(str, input().split())

    A, B = int(A[::-1]), int(B[::-1])

    if A > B:
        print(A)
    else:
        print(B)

def q5622():
    dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

    A = input()
    sum = 0
    for i in A:
        for j in dial:
            if i in j:
                B = dial.index(j) + 3
                sum += B

    print(sum)

def q11718():
    while True:
        try:
            print(input())
        except EOFError:
            break

def q1110():
    N = int(input())

    lets_start = N
    counter = 0

    while True:
        A, B = lets_start // 10, lets_start % 10

        sum = A + B

        first_digit = sum % 10

        next_number = B * 10 + first_digit

        lets_start = next_number
        counter += 1
        if N == next_number:
            break

    print(counter)

def q2577():
    A = int(input())
    B = int(input())
    C = int(input())

    D = str(A * B * C)

    counter = {'0' : 0,
            '1' : 0,
            '2' : 0,
            '3' : 0,
            '4' : 0,
            '5' : 0,
            '6' : 0,
            '7' : 0,
            '8' : 0,
            '9' : 0}

    for d in D:
        counter[d] += 1

    print(*counter.values(), sep='\n')      # * : 모든 bracket들 제거해주고 표시

def q10872():
    def factorial(n):       # failed 2 time
        if n == 0:
            return 1
        
        return n * factorial(n-1)

    N = int(input())

    print(factorial(N))

def q2558():
    A = int(input())
    B = int(input())

    print(A + B)

def q2475():
    N = map(int, input().split())

    sum = 0

    for n in N:
        sum += n ** 2

    remain = sum % 10

    print(remain)

def q3046():
    R1, S = map(int, input().split())

    R2 = 2 * S - R1

    print(R2)

def q2163():
    N, M = map(int, input().split())

    print(N * M - 1)

def q10822():
    INPUT = input()

    list = INPUT.split(',')
    sum = 0

    for l in list:
        sum += int(l)

    print(sum)

def q2455():
    total_people = 0

    max = 0

    for i in range(4):
        out_, in_ = map(int, input().split())

        total_people += in_

        total_people -= out_

        if total_people > max:
            max = total_people

    print(max)

def q2914():
    """
    저작권
    """
    A, I = map(int, input().split())

    x = (I - 1) * A + 1

    print(x)

def q2720():
    """세탁소 사장 동혁"""
    T = int(input())

    for t in range(T):

        C = int(input())

        Quarter = 0
        Dime = 0
        Nickel = 0
        Penny = 0

        while C >= 1:
            
            while C >= 5:
                
                while C >= 10:

                    while C >= 25:

                        C -= 25
                        Quarter += 1
                    
                    if C >= 10:
                        C -= 10
                        Dime += 1
                
                if C >= 5:
                    C -= 5
                    Nickel += 1

            if C >= 1:
                C -= 1
                Penny += 1

        print(Quarter, Dime, Nickel, Penny)

def q10870():
    """
    피보나치 수 5
    """
    def fibonacci(n):
        if n <= 1:
            return n
        
        return fibonacci(n-1) + fibonacci(n-2)


    number = int(input())

    print(fibonacci(number))
# -------------------- 09/22/2023 FRIDAY --------------------
def q10039():
    """
    평균 점수
    """
    number_of_students = 5
    scores = []
    sum = 0

    for i in range(number_of_students):
        scores.append(int(input()))

        if scores[i] >= 40:
            pass
        else:
            scores[i] = 40
        
        sum += scores[i]

    average = int(sum / number_of_students)
    print(average)

def q1085():
    """
    직사각형에서 탈출
    """
    x, y, w, h = map(int, input().split())

    minimum_x = min(x - 0, w - x)
    minimum_y = min(y - 0, h - y)

    if minimum_x < minimum_y:
        print(minimum_x)
    else:
        print(minimum_y)

def q11050():
    """
    이항 계수 1
    """
    N, K = map(int, input().split())

    N_result, K_result = 1, 1

    for i in range(K):
        N_result *= N
        N -= 1
        
        K_result *= K
        K -= 1

    print(int(N_result / K_result))

def q1550():
    """
    16진수
    """
    print(int(input(), 16))
# -------------------- 09/23/2023 FRIDAY --------------------
def q10156():
    """
    # 과자 한 개 가격 : K
    # 과자의 개수 : N
    # 현재 가진 돈의 액수 : M

    # 구하고자 하는 값 : K * N - M
    """
    K, N, M = map(int, input().split())

    if K * N >= M:
        needs = K * N - M
    else:
        needs = 0

    print(needs)

def q9655():
    """
    돌 게임
    """
    N = int(input())

    if N % 2 == 1:
        print("SK")
    else:
        print("CY")

def q5522():
    """
    카드게임
    """
    sum = 0

    for i in range(5):
        number = int(input())
        sum += number

    print(sum)

def q10886():
    """
    0 = not cute / 1 = cute
    """
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

def q2845():
    """
    파티가 끝나고 난 뒤
    """
    L, M = map(int, input().split())
    total = L * M
    List = [0, 0, 0, 0, 0]
    List[0], List[1], List[2], List[3], List[4] = map(int, input().split())

    difference = []
    for l in List:
        difference.append(l - total)

    print(*difference)

def q2953():
    """
    나는 요리사다
    """
    scores = []

    for i in range(5):
        scores.append(sum(map(int, input().split())))

    print(scores.index(max(scores)) + 1, max(scores))

def q5565():
    """
    영수증
    """
    total = int(input())

    for i in range(9):
        price = int(input())
        total -= price

    print(total)

def q5554():
    """
    심부름 가는 길
    """
    total = 0

    for i in range(4):
        time = int(input())
        total += time

    x, y = total // 60, total % 60
    print(x)
    print(y)