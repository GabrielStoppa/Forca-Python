import random

# Texto de inicialização
def textoInicio():
    texto = '''
                                **************************************************
                                *** Seja Bem-Vindo ao Jogo da Forca em Python! ***
                                **************************************************
    '''
    print(texto)
    print("\n")

# Faz o Desenho dos Estagios da forca
def DesenhoForca(tentativas):
    estagios = [
        """
               --------
               |      |
               |
               |
               |
               |
               -
            """,
        """
               --------
               |      |
               |      O
               |
               |
               |
               -
            """,
        """
               --------
               |      |
               |      O
               |      |
               |      |
               |
               -
            """,
        """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |
               -
            """,
        """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |
               -
            """,
        """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     /
               -
            """,
        """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """
    ]
    return estagios[tentativas]

# Abre e Escolhe alguma palavra aleatória do arquivo palavras.txt
def escolher_palavra_aleatoria(arquivo):
    with open(arquivo, 'r') as file:
        palavras = file.readlines()
    palavras = [palavra.strip().upper() for palavra in palavras]  # Remove newlines e converte para maiúsculas
    return random.choice(palavras)

# Exibe o jogo
def jogo():
    palavra_aleatoria = escolher_palavra_aleatoria('palavras.txt')
    palavra_oculta = ["_"] * len(palavra_aleatoria)
    chutes_errados = []
    tentativas = 0

    textoInicio()

    while "_" in palavra_oculta and tentativas < 6:
        print(DesenhoForca(tentativas))
        print(" ".join(palavra_oculta))  # Mostrar a palavra oculta
        print("Chutes Errados: ", " ".join(chutes_errados))  # Exibe os erros
        chute_jogador = input("Qual o seu chute? ").upper()

        # Verifica a o Acerto do Usuario
        if chute_jogador in palavra_aleatoria:
            for i in range(len(palavra_aleatoria)):
                if palavra_aleatoria[i] == chute_jogador:
                    palavra_oculta[i] = chute_jogador
            print("Você acertou! Seu chute está na palavra.")
        else:
            if chute_jogador not in chutes_errados:
                chutes_errados.append(chute_jogador)
                tentativas += 1
                print("Você errou! Seu chute não está na palavra.")

    # Finalização do Jogo
    print(DesenhoForca(tentativas))
    print(f"A palavra secreta era: {palavra_aleatoria}")
    if "_" not in palavra_oculta:
        print("\nParabéns! Você acertou a palavra secreta!")
    else:
        print("\nVocê perdeu! Tente novamente!")

# Jogar Novamente
def jogar_novamente():
    while True:
        resposta = input("\nDeseja jogar novamente? (S)im ou (N)ão ").upper()
        if resposta == 'S':
            return True
        elif resposta == 'N':
            return False
        else:
            print("Resposta inválida. Por favor, digite 'S' para sim ou 'N' para não.")

def main():
    continuar = True
    while continuar:
        jogo()
        continuar = jogar_novamente()
    print("Obrigado por jogar! Até a próxima.")

if __name__ == "__main__":
    main()
