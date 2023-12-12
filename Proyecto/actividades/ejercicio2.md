# 2.1 Instala PHP y los módulos necesarios para Apache
sudo apt install libapache2-mod-php
![imagen1](../Foto/installphp.png)  

# 2.2 Activa el módulo PHP y reinicia Apache
Primero debemos conocer la version de nuestro modulo, para ello podemos hacerlo con:
**ls /etc/apache2/mods-available/ | grep php**

sudo a2enmod php8.1(Habilitar modulo)  
![imagen1](../Foto/verificarVersionyHabilitar.png) 

sudo systemctl restart apache2  
![imagen1](../Foto/resetearApache.png) 


# 2.3 Instala el servidor de bases de datos MySQL
sudo apt install mysql-server php-mysql
![imagen1](../Foto/instalarmysql.png) 
![imagen1](../Foto/activemysql.png) 







