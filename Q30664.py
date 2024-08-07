"""
문제
Muita gente sonha em ganhar dinheiro fácil. Algumas pessoas tentam fazer isso através da loteria. Compram jogos como as “raspadinhas” e bilhetes de loteria aguardando sorteios multimilionários.

Gilmar, um rapaz muito malandro, decidiu usar seus conhecimentos matemáticos para tentar aumentar suas chances nestes jogos de sorte. Ele comprou vários bilhetes de um mesmo tipo de raspadinha e analisou as cartelas, até que percebeu uma propriedade muito curiosa: cada raspadinha tinha impresso um número identificador do cartão que permitia a ele ter noção das chances de ser premiado.

De cada 10 cartões que comprou na banca, aproximadamente 1 ou 2 vinham premiados de alguma forma: no mínimo uma outra raspadinha grátis ele ganhava, ou um prêmio simbólico em dinheiro. Quando aplicou seu método para escolher que cartões comprar, percebeu que de cada 10 cartões, em média 8 continham algum prêmio!

Como a tarefa é muito cansativa para ser feita manualmente, ele pensou que você, amigo de longa data, poderia ajudá-lo com um programa que, dado o número identificador do cartão, diz se ele faz parte do conjunto de cartões com maior chance de prêmio. O truque é procurar os cartões cujo número identificador seja múltiplo de 42. Você está apto a ajudar seu colega nesta empreitada?

입력
A entrada é composta por vários casos de teste, um por linha.

Cada caso de teste contém um inteiro n de até 30 dígitos decimais.

A entrada termina com n = 0. Este caso não deverá ser processado.

출력
Para cada caso de teste haverá uma linha na saída. Caso o número identificador do cartão seja um múltiplo de 42, imprima “PREMIADO”. Caso contrário, imprima “TENTE NOVAMENTE”.
"""

while True:
    numbers = int(input())
    if numbers == 0:
        break

    if numbers % 42 == 0:
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")