let personas = []

function agregarPersona(nombre, edad, nota) {
    personas.push({ nombre, edad, nota })
}

function mostrarDatos() {
    let listado = "Listado de personas:\n";
    personas.forEach(persona => {
        listado += `Nombre: ${persona.nombre}, Edad: ${persona.edad}, Nota: ${persona.nota}\n`;
    });
    alert(listado);
}

function mostrarDatosOrdenados() {
    let personasOrdenadas = [...personas].sort((a, b) => b.nota - a.nota);

    let listado = "Listado de personas ordenado por nota (de mayor a menor):\n";
    personasOrdenadas.forEach(persona => {
        listado += `Nombre: ${persona.nombre}, Edad: ${persona.edad}, Nota: ${persona.nota}\n`;
    });
    alert(listado);
}

function ingresarDatos() {
    let continuar = true;

    while (continuar) {
        let nombre = prompt("Ingrese el nombre de la persona:");
        let edad = parseInt(prompt("Ingrese la edad de la persona:"));
        let nota = parseFloat(prompt("Ingrese la nota de la persona:"));

        if (!nombre || isNaN(edad) || isNaN(nota)) {
            alert("Datos incorrectos. Intente nuevamente.");
            return;
        }

        agregarPersona(nombre, edad, nota);

        continuar = confirm("¿Desea ingresar otra persona?");
    }

    mostrarDatos();
    mostrarDatosOrdenados();
}


ingresarDatos() 