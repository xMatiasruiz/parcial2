def calcular_estadisticas(alumnos:dict)-> dict:
    if not alumnos:
        return None
    
    total = len(alumnos)
    suma_notas= 0 
    mayor_nota= -1
    alumno_mayor = ""
    aprobados = 0
    desaprobados = 0 

    for dni, datos in alumnos.items():
        nota = datos["nota"]
        suma_notas += nota

        if nota >= 6:
            aprobados += 1
        else:
            desaprobados += 1
        
        if nota >= mayor_nota:
            mayor_nota = nota
            alumno_mayor = f"{datos["nombre"]} {datos["apellido"]}"
    
    return{
        "total": total,
        "promedio": suma_notas / total,
        "mayor_nota": mayor_nota,
        "alumno_mayor": alumno_mayor,
        "aprobados": aprobados,
        "desaprobados": desaprobados
    }