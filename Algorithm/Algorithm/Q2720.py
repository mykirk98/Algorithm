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