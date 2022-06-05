tentativa = 1
usuario = ["eron",1234], ["helder", 3451], ["lydianne", 7698], ["pedro", 3414], ["joao", 1122]
while tentativa < 3:
    usuariotec = input("Digite o nome de usuário: ")
    senhatec = input("Digite sua senha: ")
    num = usuario.index(usuariotec)
    if usuariotec in usuario[num][0] and senhatec == usuario[num][1]:
        print("Login efetuado")
        tentativa = 4
    else:
        print('Login incorreto Tente Novamente\nTentativa {}/3'.format(tentativa))
        tentativa += 1
