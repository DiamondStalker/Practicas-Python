"""
    Ejercicio basico para crear un diccionario de datos con informacion basica de un usuario
    y validar el genero y mayoria de edad.

    El ejecicio consiste en :
        - Si es masculino:
            - Mayor de edad si tiene mas o igual a 20 anos
            - Menor de edad si tiene menos de 20
        - Si es Femenino
            - Mayor de edad si tiene mas o igual a 18 anos
            - Menor de edad si tiene menos de 18
        - En caso de que el genero no sea igual le mandaremos un error de genero ya sea porque no existe o esta mal escrito, no se tendra encuanta las mayusculas y minusculas

    Para poder imprimir edad de forma concatenda se uso str que es para pasar valores a String y poder imprimir de forma facil
"""

usuario = {
    "Nombre": "Carlos",
    "Genero": "Masculino",
    "Edad": 18
}

if(usuario["Genero"] == "Masculino"):
    if(usuario["Edad"] >= 20):
        print ("El usuario " + usuario["Nombre"] + " es mayor de edad con :" + str(usuario["Edad"]))
    else: print ("El usuario " + usuario["Nombre"] + " es menor de edad con :" + str(usuario["Edad"])) 
elif (usuario["Genero"] == "Femenino"):
    if(usuario["Edad"] >= 18):
        print ("El usuario " + usuario["Nombre"] + " es mayor de edad con :" + str(usuario["Edad"]))
    else: print ("El usuario " + usuario["Nombre"] + " es menor de edad con :" + str(usuario["Edad"])) 
