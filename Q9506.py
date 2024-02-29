while True:
    n = int(input())
    if n == -1:
        break
    divisor = []
    
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)

    if sum(divisor) == n:
        print(f"{n} = ", end='')
        for i in range(len(divisor)):
            print(divisor[i], end='')
            
            if i < len(divisor) - 1:
                print(" + ", end='')
            else:
                print()
    else:
        print(f"{n} is NOT perfect.")