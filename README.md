
<table>
  <tr>
    <td><h1>GestFerias</h1></td>
    <td><img src="static/logo.jpeg" alt="Logo" width="100"></td>
  </tr>
</table>

## La idea
La idea de este proyecto surge al observar año tras año la dificultad con la que se encuentran ayuntamientos de poblaciones cercanas que
comparten fechas de fiestas locales para la organización de estas, ya sea porque sus fiestas están
vinculadas con una festividad común como sería tener el mismo Patrón/Patrona, tener el mismo
sector industrial arraigado u otras circunstancias de las tradiciones regionales.

## Funcionalidad
Por lo que es necesaria una aplicación para facilitar dicha situación, en la cual se pretende diseñar
un espacio donde los ayuntamientos publiquen su calendario de fiestas, asignando a las mismas
las parcelas de las localizaciones donde se realizan. Dichas parcelas tienen una descripción sobre
el terreno donde se ubica (metros cuadrados, pendiente, etc.), unas coordenadas y un tipo
haciendo referencia al sector de la feria (Atracciones, Comida, Artículos y Otros) para la correcta
accesibilidad y organización de las fiestas. Impulsando de esta manera el atractivo del mundo rural
y dando más protagonismo a localidades menos conocidas. Asimismo, facilitando al sector feriante
(el cual sufrió mucho la situación sanitaria del 2020) la gestión y organización de su trabajo. Un
feriante podrá filtrar por las provincias en las que trabaje y acceder mediante el calendario de
fiestas, a los eventos, creándose así su propio calendario de recorrido concatenando fiestas, pues
al acceder a las fiestas que precise observará una descripción de esta, un mapa y un listado con
las parcelas asignadas a ella y el estado de las solicitudes que puede realizar al seleccionar las
parcelas.
Como posible fuente de ingresos y ayuda a los ayuntamientos y al resto de la sociedad también contiene
la publicitación de empresas de catering, animación y todo tipo de espectáculos o servicios. De
esta manera cualquier persona, sin la necesidad de registrarse, pueda buscar contrataciones para
sus eventos privados. Para ello, los publicitados añaden sus publicidades, una descripción de sus
servicios y los medios de contacto. Estas publicidades, una vez abonada la suscripción, son
verificadas y aprobadas por los administradores para su posterior visualización.

## Implementación
Se ha desarrollado el proyecto en un entorno Python sobre arquitectura cliente-servidor, utilizando
tecnologías modernas para el desarrollo web y tratamiento de información geoespacial. Las
herramientas y librerías utilizadas han sido las siguientes:
- Flask 3.0.3 como framework web principal.
- Jinja2 3.1.4 para la gestión de plantillas HTML dinámicas.
- Flask-SQLAlchemy 3.1.1 como ORM para el acceso a bases de datos relacionales.
- GeoAlchemy2 0.17.0 para trabajar con datos geográficos dentro de la base de datos.
- PyMySQL 1.1.1 como conector de base de datos MySQL.
- Flask-Login 0.6.3 para la gestión de sesiones de usuario.
- Flask-WTF 1.2.2 para la gestión de formularios web seguros.
- WTForms 3.2.1 para la validación de formularios.
- Shapely 2.0.6 para el tratamiento de geometrías espaciales.
- Requests 2.32.3 y HTTPLib2 0.22.0 para el consumo de servicios web externos.
- Jinja2 y Bootstrap 5 para el diseño de una interfaz web moderna y responsiva.
- XAMPP / MariaDB como entorno local de base de datos y servidor.
- Python 3.12 como lenguaje principal de desarrollo.
- Entorno virtual (venv) para el aislamiento de dependencias.
