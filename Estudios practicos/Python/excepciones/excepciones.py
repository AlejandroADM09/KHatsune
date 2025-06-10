#creando mi propia excepcion
class MiExcepcion(Exception):
    def __init__(self, mensaje):
       print(f"Se ha producido una excepción: {mensaje}")



#Lanzando la excepción
#raise MiExcepcion("Fallaste master ajajjajajajajaj")


try:
    raise MiExcepcion("Fallaste master ajajjajajajajaj")
except: #usamos except para que cuando usemos try y falle, no se detenga y salte el except. En su contra parte, si usamos else, si try no falla, se ejecuta el else
    print("fallaste")