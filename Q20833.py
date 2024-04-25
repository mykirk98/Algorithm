"""
문제
Nadja klistrar ihop små träkuber med sidlängd 1 till större kompakta kuber. Hon har nu bestämt sig för att hon vill ha en kub av varje sidlängd från 1 till N. Hur många småkuber behöver Nadja?

입력
På den första och enda raden i indatan står heltalet 
$N$, 
$1 \leq N \leq 100$.

출력
Programmet ska skriva ut en rad med ett heltal: antelet småkuber Nadja behöver.
"""

total = 0
for N in range(int(input()) + 1):
    total += N ** 3

print(total)