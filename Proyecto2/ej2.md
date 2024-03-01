## Apartado 2:
1.Primero  instalaremos Apache ejecutando el siguiente comando:  
```
sudoapt install apache2
```
2.Este comando mostrará el estado de Apache. Si Apache se ha instalado correctamente, debería mostrarse como "active" (activo) en color verde.  
![Texto alternativo](./Fotos/e2/f1-3.png)

3.Instalamos php con este comando:
```
sudo apt install php libapache2-mod-php php-mysql
```


4.Verificamos que PHP se haya instalado correctamente ejecutando el siguiente comando:
![Texto alternativo](./Fotos/e2/f1-5.png)

5.Creamos un directorio para el sitio web, le damos permisos al directorio y creamos el archivo de configuracion del virtual host.
 
![Texto alternativo](./Fotos/e2/f2-1.png)
6.Ahora dentro del nano(archivo de configuración) tenemos que escribir esta linea de comando de ejemplo :
![Texto alternativo](./Fotos/e2/f2-2.png)  

7.Lo activamos con este codigo y reseteamos para que se hagan los cambios.
![Texto alternativo](./Fotos/e2/f2-3.png)

8.Ahora con esta linea de comando entramos en hosts. 
![Texto alternativo](./Fotos/e2/f2-4.png)

9.Y configuramos la IP para nuestro proyecto. 
![Texto alternativo](./Fotos/e2/f2-5.png)

10.Ahora nos vamos al navegador y comprobaremos si funciona. 
![Texto alternativo](./Fotos/e2/f2-6.png)



