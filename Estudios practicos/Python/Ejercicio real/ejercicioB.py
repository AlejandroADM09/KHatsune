#Creando una funcion que nos devuelva numeros primos desde el 0 hasta el numero que le pasamos

def es_primo(num):
    for i in range(2,num-1):
        if num%i==0: return False
    return True


def es_primo_hasta(num):
    Primos = []
    for i in range(num):
        resultado = es_primo(i)
        if resultado == True: Primos.append(i)
    return Primos


resultado = es_primo_hasta(134)
print(resultado)