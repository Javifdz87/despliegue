# 7.1 Instalar AWStats
sudo apt install awstats

# 7.2 Configurar AWStats
sudo nano /etc/apache2/sites-available/awstats.conf

# 7.3 Agregamos las siguientes líneas al archivo de configuración
Alias /awstatsclasses "/usr/share/awstats/lib/"
Alias /awstats-icon "/usr/share/awstats/icon/"
Alias /awstatscss "/usr/share/doc/awstats/examples/css"
ScriptAlias /awstats/ /usr/lib/cgi-bin/
Options ExecCGI -MultiViews +SymLinksIfOwnerMatch

# 7.4 Habilitar el nuevo sitio y reiniciar Apache
sudo a2ensite awstats.conf
sudo systemctl restart apache2
