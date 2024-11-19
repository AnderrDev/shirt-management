from app.db import get_db

def obtener_cliente_por_usuario(usuario):
    query = "SELECT * FROM cliente WHERE usuario = %s"
    cursor = get_db().cursor(dictionary=True)
    cursor.execute(query, (usuario,))
    return cursor.fetchone()

def obtener_clientes():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cliente;")
    return cursor.fetchall()

def insertar_cliente(datos):
    db = get_db()
    cursor = db.cursor()

    sql = """
        INSERT INTO cliente (nombre, apellido, correo, rol, usuario, clave)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (
        datos['nombre'], 
        datos['apellido'], 
        datos['correo'], 
        datos['rol'], 
        datos['usuario'], 
        datos['clave']
    ))
    db.commit()
    return cursor.lastrowid  # Devuelve el ID generado automáticamente

def eliminar_cliente(id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM cliente WHERE id = %s;"
    cursor.execute(query, (id,))
    db.commit()

def actualizar_cliente(id, datos):
    db = get_db()
    cursor = db.cursor()
    query = """
    UPDATE cliente 
    SET nombre = %s, apellido = %s, correo = %s, rol = %s, usuario = %s, clave = %s
    WHERE id = %s;
    """
    valores = (datos['nombre'], datos['apellido'], datos['correo'], datos['rol'], datos['usuario'], datos['clave'], id)
    cursor.execute(query, valores)
    db.commit()
