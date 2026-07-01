from alumnos import(registrar_alumno, obtener_todos, buscar_alumnos, modificar_alumno,eliminar_alumno,data_alumnos)
from estadisticas import calcular_estadisticas
from validaciones import pedir_edad, pedir_nota
from output import mostrar_registro

def mostrar_menu():
    """
    Controla el flujo del menu principal del sistema
    """
    print("\n======== GESTIÓN DE ALUMNOS ========")
    print("1. Registrar alumno")
    print("2. Listar alumnos")
    print("3. Buscar alumno")
    print("4. Modificar alumno")
    print("5. Eliminar alumno")
    print("6. Ver estadísticas")
    print("7. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opcion⏩: ")

        if opcion == '1':
            dni = input("❎Ingrese DNI: ")
            nombre = input("❎Ingrese Nombre: ")
            apellido = input("❎Ingrese Apellido: ")
            edad = pedir_edad("❎Ingrese Edad: ")
            nota = pedir_nota("❎Ingrese Nota (0-10): ")
            
            msj_errores = registrar_alumno(dni, nombre, apellido, edad, nota)
            
            mostrar_registro(dni, msj_errores)
        
        elif opcion == '2':
            alumnos = obtener_todos()
            if not alumnos:
                print("❌No hay alumnos registrados.")
            else:
                for dni, datos in alumnos.items():
                    print("-"*20)
                    print(f"DNI: {dni}\nNombre: {datos['nombre']}\nApellido: {datos['apellido']}\nEdad: {datos['edad']}\nNota: {datos['nota']}")
        

        elif opcion == '3':
            dni= input("Ingrese el DNI a buscar: ")
            datos = buscar_alumnos(dni)
            if datos:
                print("-"*20)
                print(f"DNI: {dni}\nNombre: {datos['nombre']}\nApellido: {datos['apellido']}\nEdad: {datos['edad']}\nNota: {datos['nota']}")
            else:
                print("❌Alumno no encontrado.")
        
        elif opcion == '4':
            dni = input("Ingrese el DNI del alumno a modificar: ")
            if buscar_alumnos(dni):
                print("--- Ingrese los nuevos datos ---")
                nombre = input("Nuevo nombre: ")
                apellido = input("Nuevo Apellido: ")
                edad = pedir_edad("Nueva Edad: ")
                nota = pedir_nota("Nueva Nota (0-10): ")

                msj_errores = modificar_alumno(dni, nombre, apellido, edad, nota)
                mostrar_registro(dni, msj_errores)
            else:
                print("❌Alumno no encontrado.")

        
        elif opcion == '5':
            dni = input("Ingrese el DNI a eliminar: ")
            if eliminar_alumno(dni):
                print("❌Alumno eliminado correctamente.❌")
            else: 
                print("No se encontro el alumno con ese DNI🤨❓")


        elif opcion == '6':
            stats = calcular_estadisticas(data_alumnos)
            if stats:
                print("\n--- Estadísticas ---")
                print(f"Total alumnos: {stats['total']}")
                print(f"Promedio general: {stats['promedio']:.2f}")
                print(f"Mayor nota: {stats['mayor_nota']} ({stats['alumno_mayor']})")
                print(f"Aprobados (>=6): {stats['aprobados']}")
                print(f"Desaprobados (<6): {stats['desaprobados']}")
            else:
                print("❌No hay datos para calcular estadísticas.")
        

        elif opcion == '7':
            print("Guardando datos y saliendo del sistema. . .")
            break

        else:
            print("❌Opcion no valida, Intente nuevamente.")
