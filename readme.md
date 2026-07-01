# 🎓 Sistema de Gestión y Registro de Alumnos

Un sistema de gestión académica desarrollado íntegramente en Python puro. Este proyecto se maneja a través de una interfaz de línea de comandos (CLI) y está enfocado en la persistencia de datos mediante archivos JSON, la validación estricta de entradas y una arquitectura altamente modularizada.

## 🚀 Características Principales

* **CRUD Completo:** Permite registrar, buscar, visualizar y modificar datos de alumnos.
* **Persistencia de Datos:** Utiliza la librería estándar `json` para guardar y cargar el estado del sistema en el archivo `alumnos.json`, asegurando que la información sobreviva entre ejecuciones.
* **Validaciones Estrictas (Type Hinting):** Implementación de funciones algorítmicas manuales (sin depender de funciones mágicas externas) para validar tipos de datos, rangos numéricos (notas de 0 a 10) y longitud de cadenas.
* **Motor de Estadísticas:** Calcula en tiempo real promedios, alumno con mayor nota, y métricas de aprobados/desaprobados.
* **Diagnóstico Visual:** Sistema de reporte de errores amigable que indica al usuario exactamente qué campo falló durante la carga de datos.

## 📂 Estructura del Proyecto

El código está dividido bajo el principio de responsabilidad única para asegurar su escalabilidad y fácil mantenimiento:

* `main.py`: Punto de entrada del programa. Maneja el bucle principal, el menú de opciones y la interfaz visual.
* `alumnos.py`: Contiene la lógica central de negocio (registrar, modificar, procesar datos) y el manejo del diccionario en memoria.
* `validaciones.py`: Módulo dedicado exclusivamente al control de calidad de los datos ingresados.
* `archivos.py`: Módulo responsable de la lectura y escritura en el disco (Persistencia).
* `estadisticas.py`: Lógica de cálculo de métricas académicas.
* `output.py`: muestra el registro de una forma amigable


## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.13
* **Almacenamiento:** JSON
* **Arquitectura:** Estructurada y Modular