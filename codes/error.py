entrada = 0
try:
    divisao = 1/entrada
except ZeroDivisionError:
    print("Não é possível fazer uma divisão por 0")
except TypeError:
    print("Você precisa digitar um número")
except:
    print("Erro ao dividir")
else:
    print("Divisão é: {divisao} ")
finally:
    print("Bruno Barbosa Santos")