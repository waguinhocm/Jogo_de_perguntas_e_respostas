### Jogo de Perguntas e Respostas ###

print("Vamos Começar? Quero ver se você é bom em matemática! Vou te dar três chances.")
chance = 0
pontos = 0
while chance < 3:
    perguntas = ['Qual é a soma de 37 + 26?', 'Qual é o resultado de  13 X 17?', 'Quanto é 56 - 18?']
    respostas = ["63" , "221" , "38"]
    if pontos == (len(perguntas)*10):
        print(f"Parabéns!! Acertou todas as perguntas e fez {pontos}!!")
        break
    for i in range(len(perguntas)):
        print(perguntas[i])
        respostaUsuario = str(input("Responda: "))
        
        if respostaUsuario != respostas[i]:
            if chance < 3:
                chance += 1
                pontos = 0
                print(f"Perdeu a {chance}ª chance!")
            
            break
        else:
            pontos += 10
            
if chance >= 3:
    print("Que pena! Precisamos revisar os estudos!")