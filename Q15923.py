# x_list, y_list = [], []
# length = 0

# N = int(input())
# for n in range(N):
#     x, y = map(int, input().split())
#     x_list.append(x)
#     y_list.append(y)

#     if n == 0:
#         continue
#     else:
#         length += abs(x_list[n] - x_list[n-1]) + abs(y_list[n] - y_list[n-1])

# length += abs(x_list[-1] - x_list[0]) + abs(y_list[-1] - y_list[0])

# print(length)

x_list, y_list = [], []
length = 0
for N in range(int(input())):
    x, y = map(int, input().split())
    x_list.append(x), y_list.append(y)
    
print((max(x_list) - min(x_list) + max(y_list) - min(y_list)) * 2)