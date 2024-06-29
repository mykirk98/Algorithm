"""
문제
Your friend is a kindergarten teacher. Since the Olympic Games in Paris are approaching, he wants to teach the kids about different aspects of sports competitions. As part of this idea, he plans to have one day when kids receive medals for their behaviour in kindergarten. For example, he would give out a medal for the kid who shares their toys the most, or for the kid who encourages their playmates most creatively. To ensure kids are not offended at the end of the day, the teacher wants no kid to get fewer medals than another. The teacher tells you the number of medals he prepared and the number of kids, and he asks you to say whether it is possible to give out all of these medals to the kids so that they each get the same number of medals.

입력
The input consists of one line. This line contains two space-separated integers 
$M$ and 
$K$: 
$M$ is the number of medals and 
$K$ is the number of kids.

출력
The output should contain a single line, consisting of a word: the word Yes if it is possible to give out all 
$M$ medals to the 
$K$ kids so that each kid gets the same number of medals, or the word No otherwise.
"""

M, K = map(int, input().split())

if M % K == 0:
    print("Yes")
else:
    print("No")