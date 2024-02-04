while True:
    list_ = list(map(int, input().split()))

    if list_[0] == 0 and list_[1] == 0 and list_[2] == 0:
        break

    max_number = max(list_)
    list_.remove(max_number)

    if list_[0] ** 2 + list_[1] ** 2 == max_number ** 2:
        print("right")
    else:
        print("wrong")