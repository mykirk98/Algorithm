"""
문제
Farmer John has received an order for exactly 
\(M\) units of milk (
\(1 \leq M \leq 1,000\)) that he needs to fill right away. Unfortunately, his fancy milking machine has just become broken, and all he has are three milk pails of integer sizes 
\(X\), 
\(Y\), and 
\(M\) (
\(1 \leq X < Y < M\)). All three pails are initially empty. Using these three pails, he can perform any number of the following two types of operations:

- He can fill the smallest pail (of size 
\(X\)) completely to the top with 
\(X\) units of milk and pour it into the size-
\(M\) pail, as long as this will not cause the size-
\(M\) pail to overflow.

- He can fill the medium-sized pail (of size 
\(Y\)) completely to the top with 
\(Y\) units of milk and pour it into the size-
\(M\) pail, as long as this will not cause the size-
\(M\) pail to overflow.

Although FJ realizes he may not be able to completely fill the size-
\(M\) pail, please help him determine the maximum amount of milk he can possibly add to this pail.

입력
The first, and only line of input, contains 
\(X\), 
\(Y\), and 
\(M\), separated by spaces.

출력
Output the maximum amount of milk FJ can possibly add to the size-
\(M\) pail.
"""

# X, Y, M = map(int, input().split())

# diff = Y - X

# bucket = M // X * X

# while True:
#     if M - bucket > diff:
#         bucket += diff
#     else:
#         break

# print(bucket)


X, Y, M = map(int, input().split())

max_milk_amount = 0
for a in range(M // X + 1):  # X 물통을 몇 번 채울지
    for b in range(M // Y + 1):  # Y 물통을 몇 번 채울지
        current_milk = a * X + b * Y
        if current_milk <= M:
            max_milk_amount = max(max_milk_amount, current_milk)

print(max_milk_amount)