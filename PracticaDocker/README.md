# Guía de Docker

Esta guía proporciona una visión general de Docker y su uso, desde la instalación hasta la creación de imágenes personalizadas y la gestión de contenedores en diferentes escenarios.

## 1. Introducción a los contenedores Docker

- **Introducción a Docker:** Breve descripción de Docker y sus beneficios.
- **Instalación de Docker:** Pasos para instalar Docker en diferentes sistemas operativos.
- **El "Hola Mundo" de Docker:** Primeros pasos con Docker ejecutando un contenedor básico.
- **Ejecución simple de contenedores:** Uso básico del comando `docker run`.
- **Ejecutando un contenedor interactivo:** Interactuando con contenedores en tiempo real.
- **Creando un contenedor demonio:** Ejecución de contenedores en segundo plano.
- **Creando un contenedor con un servidor web:** Ejemplo práctico de contenedor con un servidor web.
- **Configuración de contenedores con variables de entorno:** Uso de variables de entorno en Docker.  

[Ir al ejercicio](./ej2.md)

## 2. Imágenes Docker

- **Registros de imágenes: Docker Hub:** Exploración y uso del registro público de Docker.
- **Gestión de imágenes:** Operaciones básicas con imágenes Docker.
- **¿Cómo se organizan las imágenes?:** Organización y etiquetado de imágenes.
- **Creación de contenedores desde imágenes:** Creación y ejecución de contenedores basados en imágenes.
- **Ejemplo: Desplegando la aplicación MediaWiki:** Ejemplo práctico de despliegue de una aplicación utilizando una imagen de Docker.  

[Ir al ejercicio](./ej2.md)


## 3. Almacenamiento y redes en Docker

- **Volúmenes Docker y bind mount:** Gestión de almacenamiento persistente en contenedores.
- **Asociando almacenamiento a los contenedores: volúmenes Docker:** Uso de volúmenes Docker para persistencia de datos.
- **Asociando almacenamiento a los contenedores: bind mount:** Montaje de directorios del host en contenedores.
- **Redes en Docker:** Configuración de redes para la comunicación entre contenedores.
- **Redes definidas por el usuario:** Creación y gestión de redes personalizadas.
- **Ejemplos de despliegue:**
  - **Guestbook:** Aplicación de ejemplo para demostrar el uso de redes y almacenamiento.
  - **Temperaturas:** Otro ejemplo práctico de despliegue de aplicación utilizando redes y almacenamiento.
  - **Wordpress + MariaDB:** Despliegue de una aplicación web con base de datos utilizando contenedores.
  - **Tomcat + Nginx:** Despliegue de una aplicación Java con un servidor web.  

[Ir al ejercicio](./ej2.md)

## 4. Creando escenarios multicontenedor con Docker Compose

- **Creando escenarios multicontenedor con Docker Compose:** Introducción a Docker Compose para la gestión de múltiples contenedores.
- **El fichero docker-compose.yaml:** Estructura y configuración del archivo Docker Compose.
- **El comando docker-compose:** Uso básico del comando para gestionar aplicaciones con múltiples contenedores.
- **Almacenamiento con Docker Compose:** Definición de volúmenes y montaje de directorios en Docker Compose.
- **Ejemplos de despliegue:** Mismos ejemplos anteriores utilizando Docker Compose para simplificar la gestión.

[Ir al ejercicio](./ej2.md)


## 5. Creación de imágenes en Docker

- **Creación de imágenes a partir de un contenedor:** Captura de cambios en un contenedor para crear una nueva imagen.
- **Creación de imágenes a partir de un Dockerfile:** Uso de archivos Dockerfile para definir la configuración de una imagen.
- **Distribución de imágenes:** Publicación y distribución de imágenes Docker.
- **Ejemplos de construcción de imágenes:**
  - **Página estática:** Creación de una imagen para servir una página estática.
  - **Aplicación PHP:** Construcción de una imagen para una aplicación PHP.
  - **Aplicación Python:** Creación de una imagen para una aplicación Python.
  - **Imágenes configurables:** Uso de variables de entorno para configurar imágenes.

[Ir al ejercicio](./ej2.md)


## Ciclo de vida de las aplicaciones

- **Gestión del ciclo de vida de las aplicaciones:** Consideraciones finales sobre el desarrollo, despliegue y mantenimiento de aplicaciones con Docker.

¡Disfruta aprendiendo Docker! Si tienes alguna pregunta, no dudes en consultar la documentación oficial de Docker o buscar ayuda en la comunidad.
