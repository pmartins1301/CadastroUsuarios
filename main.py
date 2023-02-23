import os.path
import time
import json
from Dicionarios.funcoes import *
from pathlib import Path

my_file= Path("bd.json")
if os.path.getsize(my_file)>0:
    pass
else:
    with open("bd.json", "w") as arquivo:
            arquivo.write("{}")



with open("bd.json", "r") as arquivo:

        usuarios = json.load(arquivo)

opcao = perguntar()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    elif opcao=="P":
        pesquisar(usuarios)
    elif opcao=="E":
        excluir(usuarios)

    else:
        listar(usuarios)

    opcao = perguntar()

