#Menu para escolher o modo de jogo
def menu():
    print("Bem-vindo ao jogo do NIM! Escolha:", end='\n\n')
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    op=int(input())
    if op == 2:
        op=1
        while op < 4:
            print("**** Rodada",op, "****\n")
            partida()
            op=op+1
        print("**** Final do campeonato! ****\n")
        print("Placar: Você 0 X 3 Computador")
    else:
        partida()
#Função que determina quantas peças a máquina pega
def computador_escolhe_jogada (n, m):
    pegapeça=0
    while pegapeça < m:
        if n%(m+1)==0:
            break
        pegapeça=pegapeça+1
        n=n-1
    if pegapeça == 0:
        pegapeça=1
    print("O computador tirou",pegapeça,"peças.")    
    return pegapeça    
#Função onde o usuário faz a sua jogada
def usuario_escolhe_jogada (n, m):
    peça=0
    while peça != 'a':
        peça=int(input("Quantas peças você vai tirar? "))
        if peça > m or peça == False:
            print("\nOops! Jogada inválida! Tente de novo.\n")
        else:
            print("Você tirou",peça,"peças.")
            break
    return peça
#Função que faz o jogo rodar
def partida ():
    n=int(input("Quantas peças? "))
    m=int(input("Limite de peças por jogada? "))
    if n%(m+1) == 0:
        print("Voce começa!", end='\n\n')
        while n != False:
            n=n-usuario_escolhe_jogada(n, m)
            if n==False:
                print("Fim do jogo! Você ganhou!")
                break
            else:
                print("Agora resta apenas",n,"peça(s) no tabuleiro.\n")
            n=n-computador_escolhe_jogada(n, m)
            if n==False:
                print("Fim do jogo! O computador ganhou!")
            else:
                print("Agora resta apenas",n,"peça(s) no tabuleiro.\n")
    else:
        while n != False:
            print("Computador começa!", end='\n\n')
            n=n-computador_escolhe_jogada(n, m)
            if n==False:
                print("Fim do jogo! O computador ganhou!")
                break
            else:
                print("Agora resta apenas",n,"peça(s) no tabuleiro.\n")
            n=n-usuario_escolhe_jogada(n, m)
            if n==False:
                print("Fim do jogo! Você ganhou!")
            else:
                print("Agora resta apenas",n,"peça(s) no tabuleiro.\n")
menu()