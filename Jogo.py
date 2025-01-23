### Jogo de Perguntas e Respostas ###

print("Vamos Começar? Quero ver se você é bom em matemática! Vou te dar três chances.")
chance = 0
while chance < 3:

    try:
        print("""Atenção à pergunta:
            
        Qual é a soma de 37 + 26? """)
        resposta = int(input("Responda: "))
        if resposta == (37+26):
            print("Parabéns! Acertou a tentativa de número - ", + (chance + 1))
            break
    except:
        print("Tente novamente.")
    chance += 1

if chance == 3:
    print("Perdeu as três chances!")