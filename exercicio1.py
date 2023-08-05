#Heitor Elias Prudente
#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def multiplas_operacoes(a, b):
    # Soma
    soma = a + b

    # Subtração
    subtracao = a - b

    # Multiplicação
    multiplicacao = a * b

    # Divisão (com tratamento para divisão por zero)
    if b == 0:
        divisao = 0
    else:
        divisao = a / b

    return soma, subtracao, multiplicacao, divisao








# Teste a sua função aqui (caso ache necessário)
print(multiplas_operacoes(2, 0))











