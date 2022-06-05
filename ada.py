#Verificação de senha
tentativa = 1
usuario = ["eron", "helder", "lydianne", "pedro", "joao"]
senha = [1234, 3451, 7698, 3412, 1122]
while tentativa < 3:
    usuariotec = input("Digite o nome de usuário: ")
    senhatec = float(input("Digite sua senha: "))
    num = usuario.index(usuariotec)
    if usuariotec in usuario and senhatec == senha[num]:
        print("Login efetuado")
        tentativa = 4
    else:
        print('Login incorreto Tente Novamente\nTentativa {}/3'.format(tentativa))
        tentativa += 1
if tentativa >3:
	print("Login bloqueado por excesso de tentativas!!!")