# Práctica 1 - Servidor de Alojamiento Web

En esta práctica, se llevará a cabo la instalación, configuración y puesta en marcha de un servidor que ofrece servicios de alojamiento web configurable. A continuación, se detallan los requisitos y pasos necesarios para completar la práctica:

## Requisitos:

1. Alojamiento de páginas web estáticas y dinámicas con PHP.
2. Asignación de un directorio de usuario con una página web por defecto.
3. Disponibilidad de una base de datos SQL administrable con phpMyAdmin.
4. Acceso de los clientes mediante FTP con configuración adecuada de TLS.
5. Habilitación del acceso mediante SSH y SFTP.
6. Automatización de tareas mediante el uso de scripts, incluyendo:
   - Creación de usuarios y directorios correspondientes para el alojamiento web.
   - Configuración de host virtual en Apache.
   - Creación de usuarios del sistema para acceso a FTP, SSH, SMTP, etc.
   - Creación de un subdominio en el servidor DNS con resolución directa e inversa.
   - Creación de una base de datos y usuario con todos los permisos sobre dicha base de datos (ALL PRIVILEGES).
   - Habilitación de la ejecución de aplicaciones Python con el servidor web.


## Pasos:

1. **Instalación y Configuración Básica del Servidor:**
   - Instalar un sistema operativo Linux en el servidor.
   - Actualizar el sistema.
   - Instalar y configurar Apache, PHP, MySQL/MariaDB, vsftpd (servidor FTP), OpenSSH (SSH).
   (La mayoria ya deberiamos de tenerlo instalado)

2. **Configuración de Apache y PHP:**
   - Configurar Apache para alojar múltiples sitios web utilizando Virtual Hosts.
   - Habilitar el módulo de PHP en Apache.
   - Reiniciar Apache.  
   [Ir al ejercicio](./ej2.md)


3. **Configuración de MySQL/MariaDB:**
   - Instalar el servidor de bases de datos.
   - Acceder al servidor MySQL/MariaDB y crear la base de datos y usuario necesario.  
   [Ir al ejercicio](./ej3.md)

4. **Instalación de phpMyAdmin:**
   - Instalar y configurar phpMyAdmin para acceder a la base de datos a través del navegador.  
   [Ir al ejercicio](./ej4.md)

5. **Configuración de vsftpd (Servidor FTP):**
   - Instalar y configurar vsftpd para permitir conexiones seguras TLS/SSL.
   - Crear usuarios FTP y asignar permisos adecuados.  
   [Ir al ejercicio](./ej5.md)

6. **Configuración de OpenSSH:**
   - Instalar y configurar OpenSSH para acceso seguro.
   - Configurar SFTP para transferencia de archivos segura.  
   [Ir al ejercicio](./ej6.md)

7. **Automatización con Scripts:**
   - Crear scripts para automatizar tareas como la creación de usuarios, configuración de Virtual Hosts, creación de bases de datos, etc.  
   [Ir al ejercicio](./ej7.md)


8. **Configuración del Servidor DNS:**
   - Configurar un servidor DNS con resolución directa e inversa.
   - Crear un subdominio y asignar resolución directa e inversa.  
   [Ir al ejercicio](./ej8.md)

9. **Ejecución de Aplicaciones Python:**
   - Configurar Apache para ejecutar aplicaciones Python utilizando mod_wsgi u otra configuración adecuada.  
   [Ir al ejercicio](./ej9.md)





