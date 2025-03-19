# Lista para almacenar las personas
personas = []

def agregar_persona(nombre, edad, nota):
    personas.append({"nombre": nombre, "edad": edad, "nota": nota})

def mostrar_datos():
    listado = "Listado de personas:\n"
    for persona in personas:
        listado += f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Nota: {persona['nota']}\n"
    print(listado)

def mostrar_datos_ordenados():
    # Ordenar las personas por la propiedad 'nota' de mayor a menor
    personas_ordenadas = sorted(personas, key=lambda x: x['nota'], reverse=True)

    listado = "Listado de personas ordenado por nota (de mayor a menor):\n"
    for persona in personas_ordenadas:
        listado += f"Nombre: {persona['nombre']}, Edad: {persona['edad']}, Nota: {persona['nota']}\n"
    print(listado)

def ingresar_datos():
    continuar = True
    while continuar:
        nombre = input("Ingrese el nombre de la persona: ")
        edad = input("Ingrese la edad de la persona: ")
        nota = input("Ingrese la nota de la persona: ")

        # Validación de los datos ingresados
        if not nombre or not edad.isdigit() or not nota.replace('.', '', 1).isdigit():
            print("Datos incorrectos. Intente nuevamente.")
            continue

        edad = int(edad)
        nota = float(nota)

        agregar_persona(nombre, edad, nota)

        continuar_respuesta = input("¿Desea ingresar otra persona? (si/no): ").lower()
        continuar = continuar_respuesta == "si"

    mostrar_datos()
    mostrar_datos_ordenados()

# Iniciar el ingreso de datos
ingresar_datos()
