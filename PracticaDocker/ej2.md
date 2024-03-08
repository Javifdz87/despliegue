# Guía para Ejercicio de Docker
## Paso 1: Verificar Docker
Primero, asegúrate de que Docker esté instalado y activado en tu sistema.

![Docker prueba hello world](./fotos/ej1/f1-1.png)

Ahora para empezar el ejercicio debemos ejecutar la imagen hello-world para ello tenemos que usar el comando:
```bash
docker run hello-world
```  
 
![Docker prueba hello world](./fotos/ej1/f1-2.png)
Este comando verifica la instalación de Docker ejecutando la imagen "hello-world".

## Paso 2: Ver imágenes y contenedores

Para ver qué imágenes Docker están instaladas, usa el siguiente comando:

```bash
docker image ls
```
Esto nos hara un listado con el repositorio, la versión descargada, la id de la imagen, cuando se creo y el tamaño que ocupa:  
![Docker prueba image ls](./fotos/ej1/f1-3.png)


Este comando proporciona una lista de las imágenes Docker instaladas en tu sistema.

Para ver todos los contenedores Docker, ya sea en ejecución o no, usa:
```bash
docker container ls -a
```  

![Docker container ls -a](./fotos/ej1/f1-4.png)
Este comando muestra una lista de todos los contenedores Docker en tu sistema.

## Paso 3: Crear y ejecutar un contenedor

### Primer Dockerfile  
Clona un repositorio para obtener una aplicación para probar:
```bash
git clone https://github.com/docker/getting-started.git
```  
![foto](./fotos/ej1/f1-5.png)

Edita el archivo Dockerfile. Usa un editor de texto como Nano:
```bash
sudo nano Dockerfile
```

Agrega el siguiente contenido al Dockerfile:
```bash
touch Dockerfile

# syntax=docker/dockerfile:1
   
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000
```  
![foto](./fotos/ej1/f1-6.png)

Construye el contenedor con el siguiente comando:
```bash
docker build -t getting-started .
```  
![foto](./fotos/ej1/f1-7.png)


Ejecuta el contenedor con el siguiente comando:
```bash
docker run -dp 3000:3000 getting-started
```  
Este comando ejecuta el contenedor en segundo plano, mapeando el puerto 3000 del sistema al puerto 3000 del contenedor.  
![foto](./fotos/ej1/f1-8.png)

