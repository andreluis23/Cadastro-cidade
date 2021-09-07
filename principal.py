from src.classes.Cidade import cidade
import json

sair = False
arquivo = open("./        ,"r") 
lista_cidades = json.loads(arquivo)
while sair == False:

    nome_cidade = input("Digite o nome da cidade:")
    populaçao_cidade = int(input("Digite a população da cidade:")))
    sigla_estado = input("Digite a sigla do estado:")
    nome_estado = input("Digite o nome do estado")

    uf = {"sigla": sigla_estado, "nome": nome_estado}
    nova_cidade = Cidade(nome_cidade, populacao_cidade,uf)
     
    lista_cidades.append(nova_cidade)

resposta = input("Deseja cadastrar outra cidade?")

while resposta.upper() != "S" and resposta.upper() != "N":
    print("A resposta deve ser N ou S")
    resposta =  input('Deseja cadastrar outra cidade?')
if resposta.upper () == "N":
    sair = True

print(lista_cidades)
