import json


def perguntar():
    print("\n")
    print("******************************************************")
    print("**************** Cadastro de usuários ****************")
    print("******************************************************")
    print("\n")
    return input("<I> - Para inserir um usuário\n"+
                 "<P> - Para pesquisar um usuário\n"+
                 "<E> - Para Excluir um usuário\n"+
                 "<L> - Para Listar um usuário\n\n"+
                 "O que deseja realizar? :\n").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                   input("Digite data nascimento: ").upper(),
                                                   input("Digite o CPF: ").upper()]
    salvar(dicionario)

def salvar(dicionario):
    with open("bd.json", "w") as arquivo:
        json.dump(dicionario,arquivo)



def excluir(dicionario):
    login = input("Informe o \"Login\" que deseja excluir: ").upper()
    if login in dicionario.keys():
        dicionario.pop(login)
        print("Login Excluido!")
        with open("bd.json", "w") as arquivo:
            json.dump(dicionario, arquivo)
    else:
        print("Não existe esse login")


def alterar(dicionario):
    busca = input("Informe o \"Login\" que deseja pesquisar: ").upper()

    if busca in dicionario.keys():

        print(dicionario[busca])
        dicionario["teste"] = dicionario.pop(busca)
        print(dicionario[1])
    else:
        print("Não localizado")

def pesquisar(dicionario):
    busca = input("Informe o \"Login\" que deseja pesquisar: ").upper()
    count = sum(1 for f in dicionario)
    cont = 0
    for x in dicionario:
        cont = cont + 1
        if busca != x:
            if str(cont) == str(count):
                print("\nLogin não localizado!\n")

        else:
            print("Login: " + x,
                  "\nNome: " + dicionario[f'{x}'][0],
                  "\nData nascimento: " + dicionario[f'{x}'][1],
                  "\nCPF: " + dicionario[f'{x}'][2])
            break




def listar(dicionario):
    dicionario = dict(dicionario)
    for registro, itens in dicionario.items():
        print("Login: "+registro,"\nNome: "+itens[0], "\nData de nascimento: "+ itens[1], "\nCPF: "+ itens[2]+"\n\n")