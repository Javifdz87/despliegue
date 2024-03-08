# Guía de Instalación de Docker en Ubuntu

Esta guía proporciona instrucciones paso a paso para instalar Docker en un sistema Ubuntu.

## Paso 1: Eliminar Versiones Antiguas
En este paso, estamos utilizando el gestor de paquetes apt-get para eliminar versiones antiguas de Docker y sus componentes del sistema. Esto asegura que no haya conflictos ni versiones obsoletas que puedan interferir con la instalación de la nueva versión.
```bash
$ sudo apt-get remove docker docker-engine docker.io containerd runc
```

## Paso 2: Configurar Repositorio de Docker
Aquí estamos actualizando la lista de paquetes disponibles y luego añadiendo la clave GPG del repositorio de Docker para verificar la autenticidad de los paquetes descargados. Después, agregamos el repositorio oficial de Docker a la lista de fuentes de paquetes de apt.
```bash
$ sudo apt-get update
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

## Paso 3: Instalar Docker CE
En este paso, actualizamos nuevamente la lista de paquetes disponibles y luego instalamos Docker Community Edition (CE), Docker CLI y containerd.io. Esto instala los componentes principales de Docker en el sistema.
```bash
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```

## Paso 4: Verificar Estado de Docker
Finalmente, para asegurarnos de que Docker se haya instalado correctamente y esté funcionando, verificamos su estado utilizando el comando systemctl status docker. Esto nos proporciona información sobre si el servicio Docker está en ejecución y algunos detalles adicionales sobre su configuración.
```bash
$ sudo systemctl status docker
```  
![Docker prueba image ls](./fotos/ej1/f1-1.png)
