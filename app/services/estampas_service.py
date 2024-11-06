from app.db import get_db

def obtener_estampas():
    """Obtiene todas las estampas de la base de datos."""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM estampa;")
    return cursor.fetchall()

def obtener_estampa_por_id(id):
    """Obtiene una estampa específica por su ID."""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM estampa WHERE id = %s;", (id,))
    return cursor.fetchone()

def insertar_estampa(datos):
    """Inserta una nueva estampa en la base de datos."""
    db = get_db()
    cursor = db.cursor()
    query = """
    INSERT INTO estampa (codigo, titulo, color, clasificacion_id, categoria_id)
    VALUES (%s, %s, %s, %s, %s);
    """
    valores = (datos['codigo'], datos['titulo'], datos['color'], datos['clasificacion_id'], datos['categoria_id'])
    cursor.execute(query, valores)
    db.commit()

def actualizar_estampa(id, datos):
    """Actualiza una estampa existente en la base de datos."""
    db = get_db()
    cursor = db.cursor()
    query = """
    UPDATE estampa 
    SET titulo = %s, color = %s, clasificacion_id = %s, categoria_id = %s
    WHERE id = %s;
    """
    valores = (datos['titulo'], datos['color'], datos['clasificacion_id'], datos['categoria_id'], id)
    cursor.execute(query, valores)
    if cursor.rowcount == 0:
        return False
    db.commit()
    return True

def eliminar_estampa(id):
    """Elimina una estampa por su ID."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM estampa WHERE id = %s;", (id,))
    if cursor.rowcount == 0:
        return False
    db.commit()
    return True
