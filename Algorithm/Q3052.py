List = []

for i in range(10):
    number = int(input())

    if number%42 not in List:
        List.append(number%42)
    else:
        pass

print(len(List))