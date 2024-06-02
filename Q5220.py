"""
문제
In the midst of a fierce battle, Tony Stark’s suit constantly communicates with JARVIS for technical data. This data as transmitted takes the form of 16-bit integer values. However, due to various atmospheric issues (such as those created by all of that lightning Thor spreads around) there is some risk of data corruption. To help detect such corruption, for each 16-bit value that is transmitted, an additional single bit is sent. This additional single bit, called the check bit, is a 1 if the corresponding 16-bit integer has an ODD number of 1s when represented in binary. The check bit is a 0 if the corresponding 16-bit integer has an EVEN number of 1s when represented in binary. The effect is that: the number of bits set to 1 in the combined 17 bits is always EVEN.

For example, the integer 45 would appear in binary as 0000000000101101 which has an even number of 1s so the check bit would be 0. The integer 34173 would appear in binary as 1000010101111101 which has an odd number of 1s so the check bit would be 1.

입력
The first line in the test data file contains the number of test cases (< 100). After that, each line contains one test case: the first number is the 16-bit integer (provided as an int), and the following number is the check bit (also provided as an int).

출력
For each test case, you are to output “Corrupt” if the check bit doesn’t match up with the even or oddness of the integer, or “Valid” if it does.
"""

for i in range(int(input())):
    bit_integer, check_bit = map(int, input().split())

    _binary = bin(bit_integer)[2:]
    num_of_1 = _binary.count('1')

    if num_of_1 % 2 == check_bit:
        print("Valid")
    else:
        print("Corrupt")