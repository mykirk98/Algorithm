"""
문제
Ever since you started studying, your whole family have been expecting you to know the answers to a whole lot of difficult questions. What is wrong with my computer? What is the name of Prince Harry’s new girlfriend? Have you seen my new pants? Your grandfather has just found a new problem for you, and you are yet again under the pressure of finding the answers to one of life’s most fundamental questions.

You are given a 20 meter long lever balanced exactly on the middle by a massless support. A number of weights are applied to the lever. You need to figure out which side will drop, if any. Being such a brilliant mind, you immediately notice that each of the weights will contribute to the total torque applied on the lever, and that this will determine the answer. The torque from a single weight is determined by

 
\[\tau  = m \times d\] 

where 
\(\tau\) is the total torque applied, 
\(m\) is the mass of the weight and 
\(d\) is its distance from the center. The lever’s angular acceleration can then be found by the equation

 
\[\alpha = \tau / I\] 

where 
\(\alpha\) is the angular acceleration and 
\(I\) is the lever’s moment of inertia. The moment of inertia is given by the function

 
\[I = \int {r^2dm}\] 

where 
\(r\) is the perpendicular distance to the axis of rotation.

입력
The first line of input contains a single number T, the number of test cases to follow. Each test case starts with a line containing N, the number of weights in the test case. This is followed by a line containing N numbers, W1 W2 ... WN the locations of the N weights.

0 < T ≤ 100
0 < N ≤ 100
−1000 ≤ Wi ≤ 1000
A negative Wi means that the weight is located to the left of the center, while a positive one means that it is located to the right.
The weight of the lever is exactly 2000 grams, uniformly distributed. Each weight weighs 100 grams.
Weights are modeled as single point masses.
출력
For each test case, output one line containing Left if the weight tips to the left, Right if the weight tips to the right or Equilibrium if the weight does not tip to any of the sides.
"""

for T in range(int(input())):
    N = int(input())
    
    W = list(map(int, input().split()))
    
    if sum(W) == 0:
        print("Equilibrium")
    elif sum(W) > 0:
        print("Right")
    else:
        print("Left")