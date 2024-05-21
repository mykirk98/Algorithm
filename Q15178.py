"""
문제
Angela is teaching her primary school pupils how to use a protractor (which hopefully you know is a device used to measure angles!).
She has given each pupil a set of triangles and asked them to measure and record each of the three internal angles.

Angela would like you to write a simple program to check her pupil s results.
Knowing that the internal angles of a triangle add up to 180º, which results should Angela check?

입력
You will be given a set of results from one class. It will start with a single integer, N, the number of pupils who have supplied readings.
(0 < N <= 30). There will then follow N lines, each containing 3 positive integers separated by spaces.
The numbers represent the measurements supplied by a pupil for the 3 angles of a triangle.

출력
For each set of readings, output the numbers as input followed by the word Check if they do not add up to 180, or Seems OK if they do.
"""

for N in range(int(input())):
    a, b, c = map(int, input().split())
    print(f"{a} {b} {c}", "Seems OK" if a + b + c == 180 else "Check")