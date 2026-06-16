-- 1. Creación de Tablas (DDL)

CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL -- Infantil, Juvenil, Adulto
);

CREATE TABLE jugadores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria_id INT REFERENCES categorias(id),
    fecha_registro DATE DEFAULT CURRENT_DATE
);

CREATE TABLE pagos (
    id SERIAL PRIMARY KEY,
    jugador_id INT REFERENCES jugadores(id),
    mes INT NOT NULL, -- 1 para Enero, 2 para Febrero, etc.
    anio INT NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    estado VARCHAR(20) DEFAULT 'Pendiente', -- Pagado, Pendiente
    fecha_pago TIMESTAMP
);

CREATE TABLE asistencia (
    id SERIAL PRIMARY KEY,
    jugador_id INT REFERENCES jugadores(id),
    fecha DATE NOT NULL,
    estado VARCHAR(20) NOT NULL -- Presente, Ausente
);

-- 2. Poblamento Inicial (DML) - Datos de prueba para Don Rafa

INSERT INTO categorias (nombre) VALUES ('Infantil'), ('Juvenil'), ('Adulto');

-- Ejemplo de 3 jugadores (puedes añadir los 45 luego)
INSERT INTO jugadores (nombre, categoria_id) VALUES 
('Juan Pérez', 1), 
('Diego Soto', 2), 
('Luis Jara', 3);

-- Registro de pagos para probar el Dashboard
INSERT INTO pagos (jugador_id, mes, anio, monto, estado) VALUES 
(1, 5, 2026, 15000, 'Pagado'), -- Mayo
(1, 6, 2026, 15000, 'Pagado'), -- Junio (Este mes)
(2, 6, 2026, 15000, 'Pendiente'); -- Junio (Debe)

-- Registro de asistencia
INSERT INTO asistencia (jugador_id, fecha, estado) VALUES 
(1, '2026-06-10', 'Presente'),
(2, '2026-06-10', 'Ausente');