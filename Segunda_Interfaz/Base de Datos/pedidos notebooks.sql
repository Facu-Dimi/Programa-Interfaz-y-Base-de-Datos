SET foreign_key_checks = 0;

DROP SCHEMA if EXISTS pedidos_notebooks;
CREATE SCHEMA pedidos_notebooks;
USE pedidos_notebooks;

CREATE or replace TABLE Pedido(
Nro_computadora INT(4) NOT NULL PRIMARY KEY,
Alumnoo VARCHAR(90) NOT NULL,
Profesor VARCHAR(90) NOT NULL,
Fecha DATE DEFAULT CURDATE(),
Hora_de_pedido TIME DEFAULT CURTIME(),
Hora_de_entrega TIME NOT NULL);

CREATE TABLE Alumno(
Nombre_completo VARCHAR(90) NOT NULL PRIMARY key,
Curso VARCHAR(10) NOT NULL,
Especialidad VARCHAR(15) NOT NULL,
Turno VARCHAR(10) NOT NULL);

CREATE OR replace TABLE Curso(
Año_division VARCHAR(10) NOT NULL PRIMARY KEY,
Cant_compus_adquiridas INT(3)NOT NULL
);


ALTER TABLE Pedido
add FOREIGN KEY(Alumnoo) REFERENCES Alumno(Nombre_completo);

ALTER TABLE Alumno
ADD FOREIGN KEY(Curso) REFERENCES Año_division(Curso);






    

CREATE or replace TRIGGER incrementar_compus_adquiridas
after insert ON pedido
FOR EACH ROW
UPDATE curso
INNER JOIN alumno
ON alumno.curso = curso.`Año_division`
INNER JOIN pedido
ON pedido.Alumnoo = alumno.Nombre_completo
SET curso.Cant_compus_adquiridas = curso.Cant_compus_adquiridas + 1
WHERE pedido.Nro_computadora = NEW.nro_computadora
LIMIT 1;






	
	INSERT INTO curso(Año_division, cant_compus_adquiridas)
	VALUES('5to 2da', 0),
			('4to 1ra', 0);

	INSERT INTO alumno(Nombre_completo, curso, Especialidad, Turno)
	VALUES('Pablo Morales', '5to 2da', 'Computación', 'Tarde'),
			('Carlos lol', '4to 1ra', 'Construcción', 'Mañana');
			
			
	INSERT INTO pedido(Nro_computadora, alumnoo, Profesor, Hora_de_entrega)
	VALUES (783, 'Pablo Morales', 'Maximo Pereira', '08:23:00');
	
	INSERT INTO alumno(Nombre_completo, curso, Especialidad, Turno)
	VALUES('Juano lol', '3ro 2da', 'Computación', 'Tarde');

			 
SELECT * FROM pedido;

DESCRIBE pedido;

SELECT * FROM curso;

SELECT * FROM alumno