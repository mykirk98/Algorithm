"""
문제
Axel vill tävla med Petra om vem som sålt flest äpplen respektive päron, men Petra tycker inte att man kan "jämföra äpplen och päron". De kommer överens om att de istället ska jämföra hur mycket de tjänat. De ber dig skapa ett program som skriver ut vem som tjänat mest. Äpplen kostar 7 kronor styck och päron 13 kronor styck.

입력
En rad med två heltal 
$A,P$ (
$0 \le A,P \le 1000)$, antalet äpplen Axel har lyckats sälja, och antalet päron Petra har lyckats sälja. 

출력
Programmet ska skriva ut en rad med en sträng: den person som har tjänat mest, "Axel" eller "Petra". Om de sålt för lika mycket ska du skriva "lika".
"""

A, P = map(int, input().split())

A *= 7
P *= 13

if A > P:
    print("Axel")
elif A == P:
    print("lika")
else:
    print("Petra")