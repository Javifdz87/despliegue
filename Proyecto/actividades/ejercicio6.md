# 6.1 Instalar htpasswd
sudo apt install apache2-utils

# 6.2 Crear un archivo de usuarios y configurar la autenticación
sudo htpasswd -c /etc/apache2/.htpasswd usuario
sudo nano /etc/apache2/sites-available/departamentos.centro.intranet.conf  

# 6.3 Agregamos esta linea de codigo en Apache.
<VirtualHost *:80>  
    ServerName departamentos.centro.intranet
    DocumentRoot /var/www/html/departamentos.centro.intranet

    WSGIScriptAlias / /var/www/html/departamentos.centro.intranet/app.py

    <Directory /var/www/html/departamentos.centro.intranet>
        WSGIProcessGroup app
        WSGIApplicationGroup %{GLOBAL}
        Require valid-user
        AuthType Basic
        AuthName "Acceso restringido"
        AuthUserFile /etc/apache2/.htpasswd
    </Directory>
</VirtualHost>

# 6.4 Habilitar el nuevo sitio y reiniciar Apache
sudo a2ensite departamentos.centro.intranet.conf
sudo systemctl restart apache2