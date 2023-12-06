# 8.1 Instalar Nginx
sudo apt install nginx

# 8.2 Configurar Nginx
sudo nano /etc/nginx/sites-available/servidor2.centro.intranet

# 8.3 Agrega las siguientes líneas al archivo de configuración:
server {
    listen 8080;
    server_name servidor2.centro.intranet;

    root /var/www/html/servidor2.centro.intranet;
    index index.php index.html index.htm;

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }

    location /phpmyadmin {
        alias /usr/share/phpmyadmin/;
        index index.php index.html index.htm;
    }

    location ~ /\.ht {
        deny all;
    }
}

# 8.4 Habilitar el nuevo sitio y reiniciar Nginx
sudo ln -s /etc/nginx/sites-available/servidor2.centro.intranet /etc/nginx/sites-enabled/
sudo systemctl restart nginx

# 8.5 Instalar phpMyAdmin
sudo apt install phpmyadmin

# 8.6 Configurar phpMyAdmin
sudo ln -s /etc/phpmyadmin/apache.conf /etc/nginx/conf.d/phpmyadmin.conf
sudo systemctl restart nginx