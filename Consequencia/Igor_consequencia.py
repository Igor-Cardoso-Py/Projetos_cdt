'''



Primicias

Criar um lista de desejos para o futuro

---Carregar desejos existentes
'r' significa modo de leitura (read)
'with open (...) as f:' garante que o arquivo seja fechado


---Funcçao para salvar os desejos

---loop Principal do programa
'''


print ("Minha lista de desejos para o futuro \n")

NOME_ARQUIVO = "meus_desejos.txt"
desejos = []

try: 
    print(f"Meus desejos foram carrgados do arquivo '{NOME_ARQUIVO}'! \n")
except FileNotFoundError:
    print(f"Parece que é a sua primeira vez! Vamos criar sa lista de desejos.\n") except Exception as e:

print (f"Ocorreu um erro ao carregar os desejos: {e}")

def salvar_desejos(lista_de_desejos):
    try:
        with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
            for desejo in lista_de_desejos:
                arquivo.write(desejo + "\n")
                print ("\n Seus desejos foram salvos com sucesso!")
            except Exception as e:
print (f"\n Erro ao salvar os desejos: {e}")

while True:
    print ("\n---Oque voçê que fazer?---")
    print("1 - Adicionar um novo desejo")
    print("2 - Ver meus desejos")
    print("3 - Sair")

    opcao = input ("Digite sua opãp (1, 2 ou 3):")
    if opcao == "1":
        novo_desejo = input("Qual é o seu novo desejo para o futuro?")
        if novo_desejo.strip():
            desejos.append(novo_desejo.strip())
            salvar_desejos(desejos)



