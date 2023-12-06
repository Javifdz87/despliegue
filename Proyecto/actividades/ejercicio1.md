# 1.1 Debemos de instalar Apache:
sudo apt update  
![imagen1](../Foto/update.jpg)  
sudo apt install apache2  
![imagen2](../Foto/apacheInstall.png)


# 1.2 Abre el archivo hosts en un editor de texto.
sudo nano /etc/hosts
![imagen3](../Foto/sudo%20nano.jpg)


# 1.3 Agregar las siguientes líneas en el sudo nano.
127.0.0.1       centro.intranet  
127.0.0.1       departamentos.centro.intranet  
127.0.0.1       servidor2.centro.intranet  
![imagen4](../Foto/GNU%20nano.jpg)

