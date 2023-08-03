#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def tem_duplicados(lista):
    num = set()
    for i in lista:
        if i in num:
            return True
        num.add(i)
    return False
        







# Teste a sua função aqui (caso ache necessário);







