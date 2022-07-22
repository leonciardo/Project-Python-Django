Proyecto PintaManos

-Descripcion general

Pintamanos es una web creada por estudiantes de python en el curso de CoderHouse, con el proposito
de demostrar nuestras habilidades y competencias desarrolladas durante el mismo.

En esta podran encontrar una interfaz funcional e interactiva, con distintas funcionalidades, 
las cuales van desde la creacion y logueo de usuarios, control de permisos desde el panel de administrador,
creacion, edicion y eliminacion de informacion desde el panel de Staff.


- Requisitos.
Intalacion de las siguientes extensiones:
 - Django
 - Pillow
 - Python


-Instalacion
En alguna carpeta de su directorio ejecute los siguientes pasos.
- Abrir git bash desde la carpeta deseada
- ejecutar la siguiente linea: git clone https://github.com/leonfio1515/Copertini-Mesaglio-Fiorentino.git
- pip install pillow
- pip install django
- pip install python


- Funcionamiento
Al ingresar al host se podra acceder al inicio desde la ruta raiz.
Cada uno de los botones de la barra de navegacion son funcionales y operativos, por lo que 
sera redirigido a una nueva pagina segun selecciones.
Dentro de cada una podra encontrar distintos botones que le ampliaran informacion, como lo es dentro del 
menu de noticias, donde vera un resumen de ellas, pero podra acceder individualmente para ver toda la informacion
de la seleccionada.
Cuanta con una seccion de contacto donde podra escribirle directamente al administrador de la web y un 
apartado "acerca de" donde encontrara informacion de los desarrolladores
Algunas secciones estan restrigidas a usuarios registrados o miembros del staff

.Para los miembros de Staff
Podra encontrar dentro del menu de usuario, la posibilidad de crear o editar noticias, donde cada una tendra
distintas caracteristicas.
Podra acceder a la informacion de los alumnos inscriptos donde veran informacion relacionada a los mismos
.Para usuarios registrados.
Podran encontrar dentro del menu de usuarios, la posibilidad de editar sus datos de perfil,
asi como la opcion dentro de cursos de inscribirse a uno de ellos.

-Desarrollo.
	.Leonardo Mesaglio
		-Toda la seccion de Noticias.
		-Toda la seccion de "Acerca de"
		-CBV de "Noticias"
		-Todo "Inicio"	
		-CRUD alumnos

	.Federico Copertini
		-Toda la seccion de "Cursos"
		-CRUD completo para "Cursos" con usuario Staff
		-CBV de "Cursos"
                -Testeo con test.py

	.Leonardo Fiorentino
		-Login, logout, registro, edicion de perfil
		-Toda la seccion de Profesores.
		-Creacion y edicion de noticias, desde perfil Staff.
		-Seccion de "Contacto", y list de Mensajes en perfil Staff.
		-Formulario inscripcion a cursos.
		
	Enfoque estetico y detalles visuales.
		-Botones, imagenes, diseños aplicados de Bootstrap, estilos, enlaces externos.
			.Leonardo Mesaglio, Federico Copertini, Leonardo Fiorentino


- Los creadores.
.Leonardo Mesaglio
.Fernando Copertini
.Leonardo Fiorentino			

- Agradecimientos.
A todo el equipo de Coder por el apoyo y seguimiento en estos meses de desarrollo, y mencion para 
Rodrigo Robert quien fue nuestro tutor y estuve pendiente de nuestras necesidades en cada desafio, asi como
para Lucas Trubiano, quien guio cada una de las clases y nos brindo excelente apoyo y ejemplos que nos sirvieron
para desarrollarnos mas cada dia
