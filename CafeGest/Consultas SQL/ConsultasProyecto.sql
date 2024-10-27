create database cafeteria;

use cafeteria;


create table usuarios(
id int auto_increment  primary key not null,
nombre varchar(50),
apellido varchar(50)
);

insert into usuarios values(null,"Santiago","Gallego");
select * from cafeteria.usuarios;
insert into usuarios values(2,"Daniel","Zapata");
UPDATE usuarios SET usuarios.nombre = 'Mauricio',usuarios.apellido = 'Salazar'Where usuarios.id = 8;
DELETE from usuarios WHERE usuarios.id = 10;

create table productos(
idProducto int auto_increment  primary key not null,
nombreProducto varchar(50),
precioUnitario int,
disponibilidad int
);
insert into productos values(null,"Platanitos",1200,50);
select * from productos;
insert into cafeteria.productos values(2,"Milo",1800,20);
insert into cafeteria.productos values(3,"Perro Caliente",3000,15);

create table cafeteria.proveedores(
idProveedor int auto_increment  primary key not null,
nombreProveedor varchar(50),
telefono varchar(15),
producto varchar (25)
);

insert into cafeteria.proveedores values(2,"Panaderia","3216987541","Pan agridulce");