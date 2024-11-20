from app.db import get_db

def obtener_camisetas():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM camiseta;")
    return cursor.fetchall()

def insertar_camiseta(datos):
    db = get_db()
    cursor = db.cursor()
    query = """
    INSERT INTO camiseta (talla, color, material, precio)
    VALUES (%s, %s, %s, %s);
    """
    valores = (datos['talla'], datos['color'], datos['material'], datos['precio'])
    cursor.execute(query, valores)
    db.commit()

def eliminar_camiseta(id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM camiseta WHERE id = %s;"
    cursor.execute(query, (id,))
    db.commit()

def actualizar_camiseta(id, datos):
    db = get_db()
    cursor = db.cursor()
    query = """
    UPDATE camiseta 
    SET talla = %s, color = %s, material = %s, precio = %s
    WHERE id = %s;
    """
    valores = (datos['talla'], datos['color'], datos['material'], datos['precio'], id)
    cursor.execute(query, valores)
    db.commit()
