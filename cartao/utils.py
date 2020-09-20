import random


def pontuacao_credito ():
    return str(random.randint(1,999))

def aprovacao():
    if int(pontuacao_credito())<=299:
        return False

def credito_dado():
    if int(pontuacao_credito ()) <= 299:
        print(0)
    elif (int(pontuacao_credito ()) >=300) and (int(pontuacao_credito ())<= 599):
         print(1000)
    elif (int (pontuacao_credito ()) >= 600) and (int (pontuacao_credito ()) <= 799):
        print(0.5)
    elif (int (pontuacao_credito ()) >= 800) and (int (pontuacao_credito ()) <= 950):
        print(2)
    else :
        print(1000000)




