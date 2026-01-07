# Optimizando imagenes Docker

La optimización es importante; la reducción del tamaño de nuestra imagen Docker nos va a permitir ahorrar costos. 

En el siguiente ejemplo vamos a dockerizar una aplicación con React y vamos a reducir su tamaño.

## Dockerizamos nuestra aplicacion

Primero nos colocamos en la carpeta reactapp, luego creamos el archivo Dockerfile

```sh
FROM node:18

WORKDIR /app
COPY app /app
RUN npm install -g webserver.local
RUN npm install && npm run build

EXPOSE 3000
CMD webserver.local -d ./build
```

Construimos la imagen con el comando

```
docker build -t reactapp .
```

Para ver el tamaño de la imagen usamos el comando ```docker image ls```

<p align="center">
<img src="img/reactapp1.jpg" style="max-width: 400px;">
</p>

Observamos que la imagen pesa 1.35 GB
