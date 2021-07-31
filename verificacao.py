while True:
    #Verificar tamanho dos nomes e avalaiar eles!
    print("\n"*120)
    parar = ''
    nome = str(input("Digite seu nome de usuario:\n"))
    idade = int(input("Digite sua idade:\n"))

    def verificar_texto_tamanho(nome, idade):
        if len(nome) >= 10:
            print(f"Opa! O seu nome: {nome} Possui {len(nome)} Caracteres! e é muito grande!")
        elif nome == "Davu" and idade == 16:
            print(f"Bem-Vindo {nome} de volta!")
        elif nome == "Davu" and idade != 16:
            print(f"você errou o login e tentou acessar a conta de {nome}, seu safado!")
        else:
            imprimir(nome, idade)
            verificar_idade(idade, nome)
    def verificar_idade(idade):
            if idade <= 18:
                print(f"você tem idade para participar {idade}")
            else:
                print(f"Você não tem idade para participar {idade}")
    def imprimir(nome, idade):
        print(f"O nome: {nome} possui {len(nome)} Caracteres.")
        verificar_idade(idade, nome)
        return print(verificar_idade(nome, idade))

    nome = verificar_texto_tamanho(nome, idade)
    
    parar = str(input("Deseja continuar? y//n: \n"))
    if parar == "n":
        print("você parou")
        break
