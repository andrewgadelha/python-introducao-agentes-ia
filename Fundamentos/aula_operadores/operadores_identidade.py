
lista_a = [1, 2, 3]
lista_b = lista_a       # As duas variáveis apontam para o mesmo objeto.
lista_c = [1, 2, 3]     # Mesmo conteúdo, mas é outro objeto.

print(lista_a is lista_b)      
print(lista_a is lista_c)       
print(lista_a is not lista_c)   

valor = None
print(valor is None)            # True: forma recomendada para verificar None.