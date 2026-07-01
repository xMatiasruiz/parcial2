def validar_edad(edad: int)-> bool:
    """
    Valida que la edad ingresada no sea un numero negativo.
    Args:
        edad(int): El numero que representa la edad del usuario.
    
    Returns:
        bool: True si la edad es mayor o igual a 0, False si es negativa.
    """
    if edad >= 0:
        return True
    else:
        return False
    
def adulto(edad: int)-> bool:
    """
    Verifica si la persona es mayor de edad.

    Args:
        edad (int): La edad a evaluar.

    Returns:
        bool: True si tiene 18 años o más, False si es menor.
    """
    if edad >= 18:
        return True
    else:
        return False
    
    
def validar_nota(nota:float)-> bool:
    """
    Valida que la nota esté dentro del rango permitido (0 a 10).

    Args:
        nota (float/int): La calificación numérica ingresada.

    Returns:
        bool: True si la nota está entre 0 y 10 (inclusive), False en caso contrario.
    """
    if nota >= 0 and nota <= 10:
        return True
    else:
        return False


def validar_dni(dni:str) -> bool:
    """
    Valida que el DNI ingresado tenga la longitud mínima requerida.

    Args:
        dni (str): El DNI ingresado en formato de texto.

    Returns:
        bool: True si el DNI tiene 7 o más caracteres, False si tiene menos.
    """
    if len(dni) >= 7:
        return True
    else:
        return False
    

def validar_nombre(nombre:str)-> bool:
    """
    Valida que el nombre o apellido ingresado tenga una longitud mínima.

    Args:
        nombre (str): El texto correspondiente al nombre o apellido.

    Returns:
        bool: True si tiene 4 o más caracteres, False si tiene menos.
    """
    if len(nombre) >= 4:
        return True
    else:
        return False
    

def validar_solo_letras(texto:str)-> bool:
    """
    Verifica que el texto ingresado contenga únicamente letras y espacios, 
    sin números ni caracteres especiales.

    Args:
        texto (str): La cadena de texto a evaluar.

    Returns:
        bool: True si todos los caracteres pertenecen al abecedario permitido, 
            False si encuentra algún carácter no válido.
    """
    letras_permitidas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚñÑ "
    
    for caracter in texto:
        # Si encuentra un solo carácter que no este en nuestro abecedario (ej: un número), falla
        if caracter not in letras_permitidas:
            return False
            
    return True


def pedir_edad(mensaje:str)-> int:
    """
    Solicita al usuario que ingrese su edad y asegura que el valor 
    sea un número entero válido, atrapando posibles errores de tipeo.

    Args:
        mensaje (str): El texto que se mostrará por consola para pedir el dato.

    Returns:
        int: La edad convertida exitosamente a número entero.
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: ingrese un numero entero valido")
        

def pedir_nota(mensaje:str)-> float:
    """
    Solicita al usuario que ingrese una nota y asegura que el valor 
    sea un número decimal (float) válido, atrapando posibles errores.

    Args:
        mensaje (str): El texto que se mostrará por consola para pedir la nota.

    Returns:
        float: La nota convertida exitosamente a número decimal.
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: ingrese un numero valido (ej: 8.0 o 8.5)")
