CREATE SCHEMA `blog` ;

CREATE TABLE `blog`.`usuario` (
  `id` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(45) NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `contraseña` VARCHAR(45) NOT NULL,
  `estado` TINYINT NOT NULL,
  `fecha_creacion` DATE NOT NULL,
  `avatar` VARCHAR(45) NOT NULL,
  `es_publico` TINYINT NOT NULL,
  `es_colaborador` TINYINT NOT NULL,
  `es_admin` TINYINT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE);
  
  CREATE TABLE `blog`.`articulo` (
  `id` INT NOT NULL,
  `id_usuario` INT NOT NULL,
  `titulo` VARCHAR(45) NOT NULL,
  `resumen` VARCHAR(45) NULL,
  `contenido` VARCHAR(255) NULL,
  `fecha_publicacion` DATE NOT NULL,
  `estado` TINYINT NOT NULL,
  `imagen` VARCHAR(255) NULL,
  PRIMARY KEY (`id`),
  INDEX `id_usuario_idx` (`id_usuario` ASC) VISIBLE,
  CONSTRAINT `id_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `blog`.`usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
    
CREATE TABLE `blog`.`comentario` (
  `id` INT NOT NULL,
  `id_articulo` INT NOT NULL,
  `id_usuario` INT NOT NULL,
  `contenido` VARCHAR(255) NOT NULL,
  `fecha_hora` DATETIME NOT NULL,
  `estado` TINYINT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `id_articulo_idx` (`id_articulo` ASC) VISIBLE,
  INDEX `id_usuario_idx` (`id_usuario` ASC) VISIBLE,
  CONSTRAINT `fk_id_articulo`
    FOREIGN KEY (`id_articulo`)
    REFERENCES `blog`.`articulo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_id_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `blog`.`usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
    
CREATE TABLE `blog`.`categoria` (
  `id` INT NOT NULL,
  `id_categoria` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(45) NOT NULL,
  `imagen` VARCHAR(255) NULL,
  `estado` TINYINT NOT NULL,
PRIMARY KEY (`id`));

ALTER TABLE `blog`.`categoria` 
ADD INDEX `fk_id_categoria_idx` (`id_categoria` ASC) VISIBLE;
;
ALTER TABLE `blog`.`categoria` 
ADD CONSTRAINT `fk_id_categoria`
  FOREIGN KEY (`id_categoria`)
  REFERENCES `blog`.`categoria` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
CREATE TABLE `blog`.`categoria_articulo` (
  `id_articulo` INT NOT NULL,
  `id_categoria` INT NOT NULL,
  INDEX `fk2_id_articulo_idx` (`id_articulo` ASC) VISIBLE,
  INDEX `fk2_id_categoria_idx` (`id_categoria` ASC) VISIBLE,
  CONSTRAINT `fk2_id_articulo`
    FOREIGN KEY (`id_articulo`)
    REFERENCES `blog`.`articulo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk2_id_categoria`
    FOREIGN KEY (`id_categoria`)
    REFERENCES `blog`.`categoria` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
    
/*- Agregar el comando necesario que introduzca en la tabla usuario, 1 usuario con rol
de admin, 4 con rol de colaborador y 5 con rol de público. Donde los campos:
es_publico, es_colaborador y es_admin son booleanos. */
INSERT INTO `blog`.`usuario`
VALUES (1,'Celeste','Swift','3333444444','cele-23','12345',0,'2023-06-06','avatar1',1,0,0),
(2,'Maria','Sanchez','3333444444','cmaria_2023','12345',1,'2023-05-16','avatar2',1,0,0),
(3,'Carlos','Taboada','3333444444','carlos1943','4563',0,'2023-06-05','avatar3',1,0,0),
(4,'Sara','Machado','3333444444','machado_s','1sara45',1,'2023-05-06','avatar4',1,0,0),
(5,'Milton','Gomez','3333444444','milton23','321fds',0,'2023-05-26','avatar5',1,0,0),
(6,'Aria','Stark','3333444444','aria23','fdasvcxz',1,'2023-05-20','avatar6',0,1,0),
(7,'Brisa','Alvarez','3333444444','alvarez34','jhfgtre',0,'2023-05-22','avatar7',0,1,0),
(8,'Belen','Vucko','3333444444','belen20','bvcxgfd',1,'2023-05-24','avatar8',0,1,0),
(9,'Pablo','Perez','3333444444','granito','fjcmsn',0,'2023-06-22','avatar9',0,1,0),
(10,'Marcos','Tortosa','3333444444','marcos45','3fdsvcxzhg',1,'2023-05-01','avatar10',0,0,1);

/* - Agregar el comando necesario para actualizar el rol a admin de uno de los usuarios
agregado con rol de colaborador. */
update usuario set es_admin = 1, es_colaborador = 0 where es_colaborador = 1 limit 1;

/* - Agregar el comando necesario que introduzca en la tabla articulo, 3 artículos con
estado TRUE y uno con estado FALSE. Donde el campo estado en todas las tablas es
Booleano. */
INSERT INTO blog.articulo
VALUES 
(1,2,'Beneficios de hacer ejercicio diario','Descubre cómo el ejercicio diario puede mejorar tu salud y bienestar.', 'El ejercicio regular tiene numerosos beneficios para el cuerpo y la mente. Ayuda a mantener un peso saludable, fortalece los músculos, mejora la salud cardiovascular y reduce el estrés.','2023-05-16',1,'https://example.com/imagen1.jpg'),
(2,7,'Consejos para una alimentación equilibrada','Aprende a llevar una dieta equilibrada para mantener una buena salud.','Una alimentación equilibrada es clave para obtener los nutrientes necesarios y mantener un peso saludable. Incluye una variedad de alimentos como frutas, verduras, proteínas magras y granos enteros.','2023-06-02',1,' https://example.com/imagen2.jpg'),
(3,10,'Técnicas para mejorar la concentración','Descubre cómo puedes aumentar tu enfoque y concentración en tus tareas diarias.','La concentración es fundamental para ser productivo y alcanzar tus metas. Algunas técnicas efectivas incluyen eliminar distracciones, establecer metas claras y practicar la atención plena.','2023-06-01',1,'https://example.com/imagen3.jpg'),
(4,6,'Consejos para un sueño reparador','Mejora la calidad de tu sueño con estos consejos prácticos.','Dormir lo suficiente y tener un sueño reparador es esencial para mantener una buena salud. Establecer una rutina de sueño, crear un ambiente propicio para descansar y evitar el consumo de cafeína antes de dormir son algunas recomendaciones.','2023-05-29',0,'https://example.com/imagen4.jpg')
;

/* - Agregar el comando necesario para eliminar el artículo que tenga estado FALSE. */
DELETE FROM articulo WHERE id = (SELECT id FROM (SELECT * FROM articulo WHERE estado = 0) AS subquery);

/* - Agregar el comando necesario que introduzca 3 comentarios al primer artículo
agregado y 2 comentarios al segundo artículo. */
INSERT INTO comentario
VALUES (1,1,3,'Excelente artículo, muy informativo. ¡Gracias por compartir!','2023-07-16 10:06:01',0),
(2,1,4,'Me gustó mucho el enfoque del tema. ¡Sigue así!','2023-06-29 23:05:13',1),
(3,1,2,'Interesante lectura. Aprendí mucho de este artículo.','2023-06-30 05:04:40',0),
(4,2,8,'Buen contenido, me fue de mucha utilidad.','2023-07-01 17:17:06',1),
(5,2,9,'Buen contenido, me fue de mucha utilidad.','2023-07-03 06:07:30',0);

/* - Agregar el comando necesario para listar todos los artículos que tengan
comentarios, mostrando el título del artículo, la fecha_publicacion del artículo, el
nombre del usuario que realizo el comentario y la fecha_hora que realizó dicho
comentario, agrupados por artículos.*/
SELECT articulo.titulo, articulo.fecha_publicacion, usuario.nombre, comentario.fecha_hora, comentario.contenido
FROM comentario
JOIN articulo ON comentario.id_articulo = articulo.id
JOIN usuario ON comentario.id_usuario = usuario.id;
