-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS base_camisetas;

-- Usar la base de datos
USE base_camisetas;

-- Tabla de Estampas
CREATE TABLE IF NOT EXISTS estampa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    color VARCHAR(50) NOT NULL,
    clasificacion_id INT NOT NULL,
    categoria_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Camisetas
CREATE TABLE IF NOT EXISTS camiseta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    talla VARCHAR(10) NOT NULL,
    color VARCHAR(50) NOT NULL,
    material VARCHAR(50) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Clientes
CREATE TABLE IF NOT EXISTS cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    rol VARCHAR(50) NOT NULL,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    clave VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Insertar Estampas
INSERT INTO estampa (codigo, titulo, color, clasificacion_id, categoria_id)
VALUES 
('E001', 'Estampa Roja', 'Rojo', 1, 1),
('E002', 'Estampa Azul', 'Azul', 2, 1),
('E003', 'Estampa Verde', 'Verde', 3, 2),
('E004', 'Estampa Negra', 'Negro', 1, 3);

-- Insertar Camisetas
INSERT INTO camiseta (talla, color, material, precio)
VALUES 
('S', 'Blanco', 'Algodón', 15.99),
('M', 'Negro', 'Poliéster', 18.50),
('L', 'Rojo', 'Algodón', 20.00),
('XL', 'Azul', 'Lino', 22.50);

-- Insertar Clientes
INSERT INTO cliente (nombre, apellido, correo, rol, usuario, clave)
VALUES 
('Juan', 'Perez', 'juan.perez@example.com', 'Cliente', 'juan123', 'ClaveSegura'), -- contraseña: claveSegura123
('Ana', 'Garcia', 'ana.garcia@example.com', 'Cliente', 'ana456', 'ClaveSegura'), -- contraseña: claveSegura123
('Luis', 'Martinez', 'luis.martinez@example.com', 'Administrador', 'admin789', 'ClaveSegura'); -- contraseña: claveSegura123
