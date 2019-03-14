# jogo da velha

def tela():
    def opcao(celula):
        return str(celula) if grade[celula-1] == " " else  " "
    print()
    print("    Jogo          Opções")
    print("    ====          ======")
    print()
    print(" %s | %s | %s       %s | %s | %s" %(grade[0], grade[1], grade[2], opcao(1) , opcao(2), opcao(3)))
    print("---|---|---     ---|---|---")
    print(" %s | %s | %s       %s | %s | %s" %(grade[3], grade[4], grade[5],opcao(4) , opcao(5), opcao(6)))
    print("---|---|---     ---|---|---")
    print(" %s | %s | %s       %s | %s | %s" %(grade[6], grade[7], grade[8],opcao(7) , opcao(8), opcao(9)))
    print()

def fim():
    fim = False

    # linhas
    if (grade[0] == grade[1] and grade[1] == grade[2]) and grade[0] != " " and grade[1] != " " and grade[2] != " ":
            fim = True
    if (grade[3] == grade[4] and grade[4] == grade[5]) and grade[3] != " " and grade[4] != " " and grade[5] != " ":
            fim = True
    if (grade[6] == grade[7] and grade[7] == grade[8]) and grade[6] != " " and grade[7] != " " and grade[8] != " ":
            fim = True

    # Colunas
    if (grade[0] == grade[3] and grade[3] == grade[6]) and grade[0] != " " and grade[3] != " " and grade[6] != " ":
            fim = True
    if (grade[1] == grade[4] and grade[4] == grade[7]) and grade[1] != " " and grade[4] != " " and grade[7] != " ":
            fim = True
    if (grade[2] == grade[5] and grade[5] == grade[8]) and grade[2] != " " and grade[5] != " " and grade[8] != " ":
            fim = True

    # Diagonais
    if (grade[0] == grade[4] and grade[4] == grade[8]) and grade[0] != " " and grade[4] != " " and grade[8] != " ":
            fim = True
    if (grade[2] == grade[4] and grade[4] == grade[6]) and grade[2] != " " and grade[4] != " " and grade[6] != " ":
            fim = True

    return fim


grade = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
tela()
jogador = "X"
while True :
    opcao = int(input("Opção: (0 = fim)"))
    if opcao == 0:
        break
    if opcao > 9 or opcao < 0 or grade[opcao-1] != " ":
        print("Opção não disponível ...")
        continue
    grade[opcao-1] = jogador
    tela()
    if fim():
        print("Jogador ",jogador," GANHOU!!!")
        break

    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"
