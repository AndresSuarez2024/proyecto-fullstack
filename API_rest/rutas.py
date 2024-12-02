from fastapi import APIRouter, HTTPException
from baseDeDatos import connect_to_db, get_cursor

router = APIRouter()

@router.get("/api/usuario/")
async def get_all_usuarios():
    connection = connect_to_db()
    
    if not connection:
        raise HTTPException(status_code=500, detail="Error al conectar con la base de datos.")
    
    try:
        cursor = get_cursor(connection)
        cursor.execute("SELECT * FROM usuario")
        usuarios = cursor.fetchall() 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar la base de datos: {str(e)}")
    finally:
        cursor.close()
        connection.close()
    
    return usuarios


@router.get("/api/usuario/{id}")
async def get_usuario(id: int):
    connection = connect_to_db()
    if not connection:
        raise HTTPException(status_code=500, detail="Error al conectar con la base de datos.")
    
    try:
        cursor = get_cursor(connection)
        cursor.execute("SELECT * FROM usuario WHERE id_usuario = %s", (id,))
        usuario = cursor.fetchone()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar la base de datos: {str(e)}")
    finally:
        cursor.close()
        connection.close()
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return {
        "id_usuario": usuario[0],
        "nombre": usuario[1],
        "correo": usuario[2],
        "contrasenya": usuario[3],
        "rol": usuario[4],
    }


@router.get("/api/marcaje/")
async def get_all_marcajes():
    connection = connect_to_db()
    
    if not connection:
        raise HTTPException(status_code=500, detail="Error al conectar con la base de datos.")
    
    try:
        cursor = get_cursor(connection)
        cursor.execute("SELECT * FROM marcaje")
        marcajes = cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar la base de datos: {str(e)}")
    finally:
        cursor.close()
        connection.close()
    
    return marcajes

@router.get("/api/marcaje/{id}")
async def get_marcaje(id: int): 
    connection = connect_to_db()
    
    if not connection:
        raise HTTPException(status_code=500, detail="Error al conectar con la base de datos.")
    
    try:
        cursor = get_cursor(connection)
        cursor.execute("SELECT * FROM marcaje WHERE id_marcaje = %s", (id,))
        marcaje = cursor.fetchone()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar la base de datos: {str(e)}")
    finally:
        cursor.close()
        connection.close()
    
    if not marcaje:
        raise HTTPException(status_code=404, detail="Marcaje no encontrado")
    
    return {
        "id_marcaje": marcaje[0],
        "id_usuario": marcaje[1],
        "fecha_hora_entrada": marcaje[2].isoformat(),
        "fecha_hora_salida": marcaje[3].isoformat(),
    }

