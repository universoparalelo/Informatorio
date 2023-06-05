USE productos;

INSERT INTO fabricante VALUES(1, 'Asus');
INSERT INTO fabricante VALUES(2, 'Lenovo');
INSERT INTO fabricante VALUES(3, 'Hewlett-Packard');
INSERT INTO fabricante VALUES(4, 'Samsung');
INSERT INTO fabricante VALUES(5, 'Seagate');
INSERT INTO fabricante VALUES(6, 'Crucial');
INSERT INTO fabricante VALUES(7, 'Gigabyte');
INSERT INTO fabricante VALUES(8, 'Huawei');
INSERT INTO fabricante VALUES(9, 'Xiaomi');

INSERT INTO producto VALUES(1, 'Disco duro SATA3 1TB', 86.99, 5);
INSERT INTO producto VALUES(2, 'Memoria RAM DDR4 8GB', 120, 6);
INSERT INTO producto VALUES(3, 'Disco SSD 1 TB', 150.99, 4);
INSERT INTO producto VALUES(4, 'GeForce GTX 1050Ti', 185, 7);
INSERT INTO producto VALUES(5, 'GeForce GTX 1080 Xtreme', 755, 6);
INSERT INTO producto VALUES(6, 'Monitor 24 LED Full HD', 202, 1);
INSERT INTO producto VALUES(7, 'Monitor 27 LED Full HD', 245.99, 1);
INSERT INTO producto VALUES(8, 'Portátil Yoga 520', 559, 2);
INSERT INTO producto VALUES(9, 'Portátil Ideapd 320', 444, 2);
INSERT INTO producto VALUES(10, 'Impresora HP Deskjet 3720', 59.99, 3);
INSERT INTO producto VALUES(11, 'Impresora HP Laserjet Pro M26nw', 180, 3);

/*Lista el nombre de todos los productos que hay en la tabla producto*/
SELECT nombre_producto FROM productos.producto;

-- Lista todas las columnas de la tabla producto.
SELECT * FROM productos.producto;

-- Lista el nombre de los productos y el precio en USD.
SELECT nombre_producto, precio FROM productos.producto;

-- Lista los nombres y los precios de todos los productos de la tabla producto, convirtiendo los nombres a mayúscula.
SELECT upper(nombre_producto), precio FROM productos.producto;

-- Lista los nombres y los precios de todos los productos de la tabla producto, redondeando el valor del precio.
SELECT nombre_producto, ceil(precio) FROM productos.producto;

-- Lista el código de los fabricantes que tienen productos en la tabla producto.
SELECT DISTINCT productos.fabricante.codigo_fabricante FROM productos.producto, productos.fabricante 
WHERE productos.producto.codigo_fabricante LIKE productos.fabricante.codigo_fabricante;

-- Lista los nombres de los fabricantes ordenados de forma ascendente.
SELECT nombre_fabricante FROM productos.fabricante ORDER BY nombre_fabricante;

-- Lista los nombres de los productos ordenados en primer lugar por el nombre
-- de forma ascendente y en segundo lugar por el precio de forma descendente.
SELECT nombre_producto, precio FROM productos.producto ORDER BY nombre_producto ASC, precio DESC;

-- Devuelve una lista con las 5 primeras filas de la tabla fabricante.
SELECT * FROM productos.producto WHERE codigo_producto BETWEEN 1 AND 5;

-- Lista el nombre de todos los productos del fabricante cuyo código de fabricante es igual a 2.
SELECT nombre_producto, codigo_fabricante FROM productos.producto WHERE codigo_fabricante LIKE 2;

-- Lista el nombre de los productos que tienen un precio menor o igual a 120USD
SELECT nombre_producto, precio FROM productos.producto WHERE precio <= 120;

-- Devuelve todos los productos del fabricante Lenovo. (Sin utilizar INNER JOIN).
SELECT productos.producto.nombre_producto, productos.producto.precio, productos.fabricante.nombre_fabricante 
FROM productos.producto, productos.fabricante 
WHERE productos.fabricante.nombre_fabricante LIKE 'Lenovo'; 

-- Devuelve todos los datos de los productos que tienen el mismo precio que el
-- producto más caro del fabricante Lenovo. (Sin utilizar INNER JOIN).
SELECT productos.producto.nombre_producto, productos.producto.precio, productos.fabricante.nombre_fabricante 
FROM productos.producto, productos.fabricante 
WHERE productos.producto.precio = (select max(precio) from producto, fabricante where nombre_fabricante like "Lenovo");

-- Lista el nombre del producto más caro del fabricante Lenovo.
select max(precio) from fabricante, producto where nombre_fabricante like "Lenovo";

/*Devuelve los nombres de los fabricantes que tienen productos asociados.
(Utilizando ALL o ANY). No se por el momento usar all o any*/
SELECT DISTINCT nombre_fabricante, nombre_producto FROM fabricante, producto
WHERE EXISTS (SELECT * FROM producto
  WHERE codigo_fabricante = codigo_fabricante)
ORDER BY nombre_producto;


/*querys auxiliares*/
use productos;
SELECT * FROM producto, fabricante ORDER BY fabricante.nombre_fabricante, producto.precio;
SELECT * FROM producto, fabricante ORDER BY nombre_producto;

