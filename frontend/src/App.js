import React, { useEffect, useState } from "react";

const API_URL = "http://127.0.0.1:8000/api/marcaje/";

function App() {
  const [attendanceData, setAttendanceData] = useState([]);

  useEffect(() => {
    const fetchMarcajes = async () => {
      try {
        const response = await fetch(API_URL);
        if (!response.ok) {
          throw new Error(`Error al consultar la API: ${response.statusText}`);
        }
        const marcajes = await response.json();
        setAttendanceData(marcajes);
      } catch (error) {
        console.error("Error al obtener los datos:", error);
        alert("Error al cargar los datos de la API.");
      }
    };

    fetchMarcajes();
  }, []);

  return (
    <div className="container mx-auto p-4">
      <aside className="sidebar w-1/4 float-left">
        <nav>
          <ul>
            <li className="dropdown">
              <span className="dropdown-header block py-2 font-bold">Menú</span>
              <ul className="dropdown-content">
                <li>
                  <a href="#" className="block py-1 px-2 hover:bg-gray-200">
                    Gestión de clases
                  </a>
                </li>
                <li>
                  <a href="#" className="block py-1 px-2 hover:bg-gray-200">
                    Horario
                  </a>
                </li>
                <li>
                  <a href="#" className="block py-1 px-2 hover:bg-gray-200">
                    Configuración
                  </a>
                </li>
                <li>
                  <a href="#" className="block py-1 px-2 hover:bg-gray-200">
                    Ayuda
                  </a>
                </li>
              </ul>
            </li>
          </ul>
        </nav>
      </aside>

      <main className="w-3/4 float-right">
        <header className="flex justify-between items-center bg-gray-100 p-4">
          <div className="welcome-message text-xl">
            Bienvenido/a <span className="font-bold">"Nombre profesor/a"</span>
          </div>
          <div className="header-icons flex space-x-4">
            <span role="img" aria-label="notificación">
              🔔
            </span>
            <span role="img" aria-label="mensaje">
              💬
            </span>
            <span role="img" aria-label="perfil">
              👤
            </span>
          </div>
        </header>

        <section className="content mt-4">
          <h2 className="text-2xl mb-4">Tabla de asistencia de los alumnos</h2>
          <table className="table-auto w-full border-collapse border border-gray-300">
            <thead>
              <tr>
                <th className="border border-gray-300 px-4 py-2">Nombre</th>
                <th className="border border-gray-300 px-4 py-2">Asistencia</th>
                <th className="border border-gray-300 px-4 py-2">Retraso</th>
                <th className="border border-gray-300 px-4 py-2">Marcaje</th>
              </tr>
            </thead>
            <tbody>
              {attendanceData.length > 0 ? (
                attendanceData.map((marcaje, index) => (
                  <tr key={index}>
                    <td className="border border-gray-300 px-4 py-2">
                      {marcaje.id_usuario || "Desconocido"}
                    </td>
                    <td className="border border-gray-300 px-4 py-2">
                      {marcaje.fecha_hora_entrada || "N/A"}
                    </td>
                    <td className="border border-gray-300 px-4 py-2">
                      {marcaje.fecha_hora_salida || "N/A"}
                    </td>
                    <td className="border border-gray-300 px-4 py-2">Marcaje</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td
                    className="border border-gray-300 px-4 py-2 text-center"
                    colSpan="4"
                  >
                    No hay datos disponibles
                  </td>
                </tr>
              )}
            </tbody>
          </table>
          <button className="modify-button mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
            Modificar
          </button>
        </section>
      </main>
    </div>
  );
}

export default App;
