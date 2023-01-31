from Perguntas import Perguntas

perguntas_texto = [
    "Quanto é 1+1?\n (a) 2 \n (b) 1 \n (c) 3 \n (d) 0\n\n",
    "Quanto é 2+2?\n (a) 4 \n (b) 5 \n (c) 3 \n (d) 1\n\n",
    "Quanto é 3+3?\n (a) 9 \n (b) 3 \n (c) 6 \n (d) 4\n\n"
]

perguntas = [
    Perguntas(perguntas_texto[0], "a"),
    Perguntas(perguntas_texto[1], "a"),
    Perguntas(perguntas_texto[2], "c"),
]

def perguntar(perguntas):
    pontos = 0
    for pergunta in perguntas:
        resposta = input(pergunta.pergunta)
        if(resposta == pergunta.resposta):
            print("certim")
            pontos += 1
        else:
            print("F")
    print("Você acertou: " + str(pontos) + "/" + str(len(perguntas)) + "! :-D")

perguntar(perguntas)