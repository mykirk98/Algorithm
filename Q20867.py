"""
문제
Paulina Osqulda (Osqulda är en studentikos benämning på teknologer som studerar vid Kungliga Tekniska högskolan i Stockholm, se https://sv.wikipedia.org/wiki/Osquar_och_Osqulda.) pluggar på KTH i Stockholm, och åker varje morgon till skolan via tunnelbanan. När hon kommer fram till sin tunnelbanestation måste hon åka upp längs en rulltrappa för att komma ut.

I rulltrappan bildas det ofta två olika köer. På den högra sidan av trappan ställer sig folk som vill stå still i rulltrappan, medan man ställer sig på den vänstra sidan om man föredrar att gå i rulltrappan (för att komma upp snabbare).

Paulina har märkt att det oftast bildas en jättelång kö till den vänstra sidan av rulltrappan, eftersom alla är så stressade till jobbet och vill kunna gå snabbt upp för rulltrappan. På sista tiden har hon funderat på om det kanske rentav skulle gå snabbare att istället välja den högra kön, eftersom kön där ofta är kortare.

Rulltrappan är totalt 
$M$ trappsteg lång. Om man står i rulltrappan färdas man 
$S$ trappsteg per sekund uppåt i rulltrappan. Om man istället går i rulltrappan färdas man 
$G$ trappsteg per sekund uppåt.

Totalt kan 
$A$ personer per sekund börja gå i rulltrappan ur den vänstra kön, medan 
$B$ personer per sekund kan ställa sig på rulltrappan ur den högra kön. Detta betyder att i början av förloppet går en person på rulltrappan. Innan en ny person går på rulltrappan måste denna vänta 
 
$\frac{1}{A}$ (resp 
 
$\frac{1}{B}$ sekunder) för att kunna gå på rulltrappan.

Den vänstra kön är för närvarande 
$L$ personer lång, och den högra är 
$R$ personer lång.

Hjälp Paulina avgöra vilken kö hon ska ställa sig i, för att så snabbt som möjligt nå rulltrappans topp.

입력
Den första raden i indatat består av heltalen 
$M, S, G$ som är beskrivna i uppgiften. Det gäller att 
$30 \le M \le 200$, 
$1 \le S \le G \le M$.

Nästa rad innehåller decimaltalen 
$A, B$ som är beskrivna i uppgiften. Det gäller att 
$0.1 \le A, B \le 1$.

Den sista raden innehåller heltalen 
$L, R$ som är beskrivna i uppgiften. Det gäller att 
$0 \le L, R \le 100$.

출력
Skriv ut latmask om det snabbaste alternativet är att välja den högra kön och stå i rulltrappan, eller friskus om det snabbaste alternativet är att välja den vänstra kön och gå i rulltrappan.

Det är garanterat att tiden det tar för Paulina att åka upp för rulltrappan skiljer sig med minst 1 sekund mellan de två köerna, så du behöver aldrig bry dig om fallet när båda alternativen är lika snabba.
"""

from math import ceil

M, S, G = map(int, input().split())
A, B = map(float, input().split())
L, R = map(int, input().split())

l_t, r_t = L / A, R / B

l_t += ceil(M / G)
r_t += ceil(M / S)

if l_t < r_t:
    print("friskus")
else:
    print("latmask")