# Programa: Lista de Desejos para o Futuro

print("Minha lista de desejos para o futuro \n")

NOME_ARQUIVO = "meus_desejos.txt"
desejos = []

# Função para salvar os desejos
def salvar_desejos(lista_de_desejos):
    try:
        with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
            for desejo in lista_de_desejos:
                arquivo.write(desejo + "\n")
        print("\n Seus desejos foram salvos com sucesso!")
    except Exception as e:
        print(f"\n Erro ao salvar os desejos: {e}")

# Carregar desejos existentes
try:
    with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            desejos.append(linha.strip())
    print(f"Meus desejos foram carregados do arquivo '{NOME_ARQUIVO}'! \n")
except FileNotFoundError:
    print("Parece que é a sua primeira vez! Vamos criar sua lista de desejos.\n")
except Exception as e:
    print(f"Ocorreu um erro ao carregar os desejos: {e}")

# Loop principal do programa
while True:
    print("\n---O que você quer fazer?---")
    print("1 - Adicionar um novo desejo")
    print("2 - Ver meus desejos")
    print("3 - Sair")

    opcao = input("Digite sua opção (1, 2 ou 3): ")
    if opcao == "1":
        novo_desejo = input("Qual é o seu novo desejo para o futuro? ")
        if novo_desejo.strip():
            desejos.append(novo_desejo.strip())
            salvar_desejos(desejos)
        else:
            print("Desejo não pode ser vazio.")

    elif opcao == "2":
        print("\n Seus Desejos para o Futuro:")
        if not desejos:
            print("Ainda não há desejos na sua lista.")
        else:
            for i, desejo in enumerate(desejos):
                print(f"{i + 1}. {desejo}")
        print("--------------------------")

    elif opcao == "3":
        print("Até a próxima! Continue sonhando alto!")
        break

    else:
        print("Opção inválida. Por favor, digite 1, 2 ou 3.")

