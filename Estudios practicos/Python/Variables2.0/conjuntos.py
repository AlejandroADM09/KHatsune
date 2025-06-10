#creando un conjunto con set
conjunto = set(["dato1","dato2"])

#metinedo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}


#Teoria de conjuntos

conjunto1 = {1,2,3,4,5,6,7}
conjunto2 = {1,2,3}

#Verifica si es un subconjunto o un superconjunto
"resultado = conjunto1.issuperset(conjunto2) ó resultado = conjunto1 < conjunto2"
"resultado = conjunto1.issubset(conjunto2) ó resultado = conjunto1 <= (conjunto2)"


print()