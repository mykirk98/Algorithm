"""
문제
You work at a warehouse that sells chemical products, where somebody just placed an order for all the Boron Acetate Phosphoric Carbonate (BAPC) that you have in store. This liquid is stored in many separate lots, in cube-shaped containers, but your client requires the order to be delivered in a single cube-shaped container that fits all the BAPC liquid perfectly. What should be the size of this container?

입력
The input consists of:

One line with an integer 
$n$ (
$1\leq n\leq 10^5$), the number of cube-shaped containers that you have in store.
One line with 
$n$ floating-point numbers 
$c$ (
$1\leq c\leq 10^9$), the length of one of the sides for each of these containers.
출력
Output the length of one of the sides of the cube-shaped container that will contain all the BAPC liquid.

Your answer should have an absolute or relative error of at most 
$10^{-6}$.
"""

n = int(input())
c = list(map(float, input().split()))

total_bulk = 0
for i in c:
    total_bulk += i ** 3

print(total_bulk ** (1/3))