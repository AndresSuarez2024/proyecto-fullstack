const attendanceBody = document.getElementById("attendance-body"); // El tbody de la tabla en tu HTML
const API_URL = "http://127.0.0.1:8000/api/marcaje/";

async function fetchMarcajes() {
    try {
        const response = await fetch(API_URL); // Llamada a la API
        if (!response.ok) {
            throw new Error(`Error al consultar la API: ${response.statusText}`);
        }
        const marcajes = await response.json(); // Convierte la respuesta en formato JSON

        console.log("Datos obtenidos:", marcajes); // Verifica en consola qué datos se reciben

        // Llamamos a la función para mostrar los datos en la tabla
        populateAttendanceTable(marcajes);
    } catch (error) {
        console.error("Error al obtener los datos:", error);
        alert("Error al cargar los datos de la API.");
    }
}

// Función para mostrar los datos en la tabla
function populateAttendanceTable(marcajes) {
    // Limpiar la tabla antes de agregar nuevos datos
    attendanceBody.innerHTML = "";

    // Si no hay datos, muestra un mensaje
    if (!marcajes || marcajes.length === 0) {
        const row = document.createElement("tr");
        row.innerHTML = `<td colspan="4">No hay datos disponibles</td>`;
        attendanceBody.appendChild(row);
        return;
    }

    // Recorre los datos de los marcajes y agrega filas a la tabla
    marcajes.forEach((marcaje) => {
        // Ajusta el formato de los datos si es necesario
        const idUsuario = marcaje.id_usuario || "Desconocido";
        const fechaEntrada = marcaje.fecha_hora_entrada || "N/A";
        const fechaSalida = marcaje.fecha_hora_salida || "N/A";

        // Crear una fila en la tabla
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${idUsuario}</td>
            <td>${fechaEntrada}</td>
            <td>${fechaSalida}</td>
            <td>Marcaje</td> <!-- Este campo puede ser modificado según lo que quieras mostrar -->
        `;
        attendanceBody.appendChild(row);
    });
}

// Llama a la función para cargar los datos al cargar la página
document.addEventListener("DOMContentLoaded", fetchMarcajes);
