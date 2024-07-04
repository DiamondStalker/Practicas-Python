""" 
    Un diccionario es un conjunto de informacion estructurada con orden y sentido 
    por ejemplo si quiero almacenar informacion de un usuario como:
        - Nombre
        - Edad
        - Telefono
    La estructura queda como:
"""

usuario = {
    "Nombre": "Carlos",
    "Edad": 10,
    "Materias": {
        "Matematicas" : {
            "Notas": [5,5,5,1,1],
            "NotaFinal":0
        }
    }
}

suma = 0
for i in usuario["Materias"]["Matematicas"]["Notas"]:
    suma+= i

print(usuario)


usuario["Materias"]["Matematicas"]["NotaFinal"] = suma/len(usuario["Materias"]["Matematicas"]["Notas"]) # Asignar un valor a un diccionario de datos

print(usuario)