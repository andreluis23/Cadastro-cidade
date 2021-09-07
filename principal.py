from src.classes.Cidade import cidade

sair = False
while sair == False:
     print("repetindo")

resposta = input("Deseja cadastrar outra cidade?")

while resposta.upper() != "S" and resposta.upper() != "N":
    print("A resposta deve ser N ou S")
    resposta =  input('Deseja cadastrar outra cidade?')
if resposta.upper () == "N":
    sair = True
