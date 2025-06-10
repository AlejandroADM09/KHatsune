#EJEMPLO DE IF-ELSE Y ELIF CON VARIOS IF ANIDADOS EN EL CODIGO
ingreso = 120
gasto = 60


if ingreso > 100:
    if ingreso - gasto > 50:
        print ("Estas bien")
    else:
        print ("estas gastando mucho")

elif ingreso > 50: 
    print("tienes dinero")

elif ingreso >= 10:
    print ("No tienes mucho dinero")

else:
    print("no tienes dinero")


