from validaciones import validar_edad, validar_nota, validar_dni, validar_nombre, validar_solo_letras,adulto
from archivos import cargar_datos, guardar_datos

data_alumnos = cargar_datos()

def registrar_alumno(dni:str, nombre:str, apellido:str, edad:int, nota:float)-> list:
    errores =["","","","",""]
    hubo_errores = False
                                                                #--DNI
    if dni in data_alumnos:
        errores[0]="Error: el DNI ya esta registrado"
        hubo_errores = True

    
    elif not validar_dni(dni):
        errores[0]= "Error: El DNI debe tener al menos 7 dígitos."
        hubo_errores = True

                                                                #--Nombre
    if not validar_nombre(nombre):
        errores[1]= "Error: El nombre debe tener al menos 4 letras."
        hubo_errores = True
    elif not validar_solo_letras(nombre):
        errores[1] = "El nombre no puede contener numeros ni simbolos"
        hubo_errores = True

                                                                #--Apellido
    if not validar_solo_letras(apellido):
        errores[2] = "Error: El apellido no puede contener numeros ni simbolos"
        hubo_errores = True
                                                                #--Edad
    if not validar_edad(edad):
        errores[3]= "Error: la edad no puede ser negativa."
        hubo_errores = True
    if not adulto(edad):
        errores[3]= "Error: tiene que ser mayor de edad"
        hubo_errores = True

                                                                #--Nota
    if not validar_nota(nota):
        errores[4]= "Error: la nota debe estar entre 0 y 10"
        hubo_errores = True

    
    if hubo_errores:
        return errores

    data_alumnos[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nota": nota
    }

    guardar_datos(data_alumnos)

    return ["", "", "", "", ""]


def obtener_todos():
    return data_alumnos

def buscar_alumnos(dni):
    return data_alumnos.get(dni) 

def modificar_alumno(dni:str, nombre:str, apellido:str, edad:int, nota:float)-> list:
    errores = ["","","","",""]
    hubo_errores2 = False
    if dni not in data_alumnos:
        errores[0]= "Error: El alumno no existe."
        hubo_errores2 = True


    if not validar_nombre(nombre):
        errores[1]= "Error: El nombre debe tener al menos 4 letras."
        hubo_errores2 = True
    elif not validar_solo_letras(nombre):
        errores[1] = "El nombre no puede contener numeros ni simbolos"
        hubo_errores2 = True

    if not validar_solo_letras(apellido):
        errores[2] = "Error: El apellido no puede contener numeros ni simbolos"
        hubo_errores2 = True

    
    if not validar_edad(edad):
        errores[3]= "Error: La edad no puede ser negativa."
        hubo_errores2 = True
    if not validar_nota(nota):
        errores[4]= "Error: La nota debe estar entre 0 y 10."
        hubo_errores2 = True

    if hubo_errores2:
        return errores
    
    data_alumnos[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nota": nota
    }
    guardar_datos(data_alumnos)

    return ["","","","",""]

def eliminar_alumno(dni):
    if dni in data_alumnos:
        del data_alumnos[dni]
        guardar_datos(data_alumnos)
        return True
    return False