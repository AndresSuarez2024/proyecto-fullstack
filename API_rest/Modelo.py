from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class alumno(BaseModel):
    IdAlumno: int
    IdUsuario: int
    IdCiclo: int
    IdGrupo: int

class RolEnum(str, Enum):
    Alumno = "Alumno"
    Administrador = "Administrador"
    Profesor = "Profesor"

class usuario(BaseModel):
    IdUsuario: int
    Nombre: str
    Correo: str
    Contraseña: str
    Rol: RolEnum

class administrador(BaseModel):
    IdAdministrador: int
    IdUsuario: int

class ciclo(BaseModel):
    IdCiclo: int
    Nombre_ciclo: str

class grupo(BaseModel):
    IdGrupo: int
    Nombre_grupo: str
    IdCiclo: int

class asignatura(BaseModel):
    IdAsignatura: int
    Nombre_asignatura: str
    IdCiclo: int

class EstadoEnum(str, Enum):
    Presente = "Presente"
    Retraso = "Retraso"
    Falta = "Falta"

class asistencia(BaseModel):
    IdAsistencia: int
    IdAlumno: int
    IdAsignatura: int
    IdProfesor: int
    Fecha: datetime
    Hora: int
    Estado: EstadoEnum

class marcaje(BaseModel):
    IdUsuario: int
    IdMarcaje: int
    Fecha_hora_entrada: datetime
    Fecha_hora_salida: datetime

class profesor(BaseModel):
    IdProfesor: int
    IdUsuario: int
    curso: str

class aula(BaseModel):
    IdAula: int
    Nombre_aula: str

class clase(BaseModel):
    IdClase: int
    IdAsignatura: int
    IdProfesor: int
    IdAula: int
    Fecha: datetime
    Hora_inicio: int
    Hora_fin: int

class uf(BaseModel):
    IdUF: int
    IdAsistencia: int
    IdAlumno: int
    IdAsignatura: int