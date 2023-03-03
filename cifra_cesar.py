from art import tprint
tprint("CIFRA   DE   CESARسس")

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

continuar = True
while continuar == True:
    pergunta = input("Escreva 'codificar' para codificar ou 'descodificar' para descodificar: ").lower().strip()
    if pergunta != "codificar" and pergunta != "descodificar":
        print("Inválido. Tente novamente.")
        pergunta = input(("Escreva 'codificar' ou 'descodificar': ")).lower().strip()

    mensagem = input("Escreva sua mensagem: ").lower().strip()

    numero = int(input("Número de mudança: "))
    if numero > len(alfabeto):
        print("Número inválido, tente novamente.")
        numero = int(input(f"Número de mudança (menor que {len(alfabeto)}): "))

    def cesar(mensagem, numero, pergunta):
        final = ""
        for letra in mensagem:
            if letra in alfabeto:
                posicao = alfabeto.index(letra)
                if pergunta == "codificar":
                    nova_posicao = posicao + numero
                    final += alfabeto[nova_posicao]
                elif pergunta == "descodificar":
                    nova_posicao = posicao - numero
                    final += alfabeto[nova_posicao]
            else:
                final += letra

        print(f"O resultado é {final}")

    cesar(mensagem, numero, pergunta)

    repetir = input("Você quer fazer novamente (sim/nao)?: ").lower().strip()
    if repetir == "sim":
        continuar = True
    else:
        continuar = False

