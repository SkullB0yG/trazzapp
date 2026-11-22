-- creacion de la base de datos trazzapp
create database trazzapp;

-- tabla de rol 

 create table rol (
 	id serial primary key,
 	nom_rol varchar(50) not null unique 
);

 create table estado (
 	id serial primary key,
 	nom_estado varchar(50) not null unique 
 );
 
 
 create table  usuario (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nom_usuario VARCHAR(15) NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    rol_id INT NOT NULL,
    estado_id INT NOT NULL DEFAULT 1,
   
    
    
    CONSTRAINT fk_usuario_rol
        FOREIGN KEY (rol_id)
        REFERENCES rol (id)
        ON DELETE RESTRICT,
    CONSTRAINT fk_usuario_estado
        FOREIGN KEY (estado_id)
        REFERENCES estado (id)
        ON DELETE RESTRICT
);


insert into rol (nom_rol) values('administrador');
insert into estado (nom_estado) values('activo'), ('inactivo');
insert into usuario(nombre, nom_usuario,password_hash, rol_id, estado_id)
values('keneth ojeda', 'kojeda', '12345', 1, 1);



select * from usuario;