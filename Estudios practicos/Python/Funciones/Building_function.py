#creando una funcion simple
#def saludar():
#    print("Buenas dias Alejandro, ¿Como te fue el dia de hoy?")
#saludar()


#Creando una funcion que tenga parametros, los parametro se pueden anidar con el uso de comas
def saludar(nombre,sexo):
    sexo = sexo.lower() #con esto definimos sexo = Lo pasa a minusculas
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "caballero"
    else:
        adjetivo = "crack"

    print(f"Hola {nombre}, ¿Como te fue el dia de hoy {adjetivo}, te sientes bien?")


saludar("marta", "mujer")


#Creando una contraseña aleatoria a partir de un numero que le entragamos.

def creando_una_contraseña_random(num):
    chars = "abcdefghijk"
    num_entero = str(num)
    num = int(num_entero[0])   
    c1 = num
    c2 = num - 4
    c3 = num - 7
    c4 = num + 3
    c5 = num + 4
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{chars[c4]}{chars[c5]}{num*9}"
    return contraseña


password = creando_una_contraseña_random(445)

frase = f"Master, tu contrasena va a ser: {password}"

print(frase)

