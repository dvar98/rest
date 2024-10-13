-- Crear tabla de Cliente
CREATE TABLE Cliente (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    segundo_nombre VARCHAR(100),
    apellido VARCHAR(100) NOT NULL,
    segundo_apellido VARCHAR(100),
    telefono VARCHAR(150) NOT NULL,
    correo_electronico VARCHAR(250) NOT NULL,
    rol VARCHAR(150) NOT NULL
);

-- Crear tabla de Mesas
CREATE TABLE Mesas (
    id_mesa SERIAL PRIMARY KEY,
    numero_mesa INTEGER NOT NULL,
    capacidad INTEGER NOT NULL,
    Restaurante_id_restaurante INTEGER REFERENCES Restaurante (id_restaurante)
);

-- Crear tabla de ReservasMesas (anteriormente Relation_2)
CREATE TABLE ReservasMesas (
    reservas_id_reserva INTEGER NOT NULL,
    Mesas_id_mesa INTEGER NOT NULL,
    PRIMARY KEY (reservas_id_reserva, Mesas_id_mesa),
    FOREIGN KEY (Mesas_id_mesa) REFERENCES Mesas (id_mesa),
    FOREIGN KEY (reservas_id_reserva) REFERENCES reservas (id_reserva)
);

-- Crear tabla de Reservas
CREATE TABLE reservas (
    id_reserva SERIAL PRIMARY KEY,
    nombre_reserva VARCHAR(150),
    fecha TIMESTAMP NOT NULL,
    numero_personas INTEGER NOT NULL,
    estado VARCHAR(40) NOT NULL,
    hora_reserva TIME NOT NULL,
    Cliente_id_cliente2 INTEGER NOT NULL REFERENCES Cliente (id_cliente)
);

-- Crear tabla de Restaurante
CREATE TABLE Restaurante (
    id_restaurante SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    ubicacion TEXT NOT NULL,
    telefono VARCHAR(100) NOT NULL,
    hora_apertura TIME NOT NULL,
    hora_cierre TIME NOT NULL
);
