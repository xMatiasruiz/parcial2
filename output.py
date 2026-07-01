def mostrar_registro(dni_alumno:str, errores:list)-> None:
    """
    Muestra de forma estructurada el registro
    """
    print("\n" + "=" * 60)
    print(f"REGISTRO - DNI: {dni_alumno}")
    print("=" * 60)

    tiene_errores = False
    i = 0
    while i < 5:
        if errores[i] !="":
            tiene_errores = True
        i = i + 1
    
    if tiene_errores:
        estado_formulario = "Corrija los errores"
    else:
        estado_formulario = "Aprobado y guardado en el sistema"
    
    print(f"Estado Formulario: {estado_formulario} ✔️")
    print("-" * 60)

    print("Errores detectados: ")
    hay_errores = False
    i= 0
    while i < 5:
        if errores[i] != "":
            print(f" 💢 {errores[i]}")
            hay_errores = True
        i = i + 1
    
    if not hay_errores:
        print("✔️ Ninguno, Los datos cumplen los parametros")