# Docker: De cero a experto

Material oficial del curso de **Docker** de la comunidad **Nación Cloud**. Este repositorio reúne la documentación teórica, ejemplos prácticos y aplicaciones de referencia para aprender a crear, ejecutar y desplegar contenedores desde los conceptos básicos hasta temas avanzados.

**Curso en youtube:** [Curso en Youtube](https://www.youtube.com/watch?v=aA5BBSb1X1k&list=PLt9k2f9tRGayEfn7um47fy4uxxJ2QTcWD)

**Sitio Web:** [https://nacioncloud.com/](https://nacioncloud.com/)

---

## Descripción

Docker es una plataforma que permite empaquetar aplicaciones y sus dependencias en contenedores ligeros, portables y reproducibles. En este curso aprenderás a trabajar con imágenes, contenedores, Dockerfiles, almacenamiento persistente, redes, registros de imágenes y despliegue en entornos reales.

El contenido está organizado en módulos progresivos con explicaciones, diagramas y ejercicios prácticos que puedes ejecutar en tu máquina local.

---

## Contenido del curso

| Módulo | Archivo | Temas principales |
|--------|---------|-------------------|
| 1 | [1 - Introduccion.md](1%20-%20Introduccion.md) | Qué es Docker, arquitectura, VMs vs contenedores, instalación |
| 2 | [2 - Imagenes y contenedores.md](2%20-%20Imagenes%20y%20contenedores.md) | Imágenes, contenedores, ciclo de vida, comandos básicos |
| 3 | [3 - Dockerfile.md](3%20-%20Dockerfile.md) | Estructura del Dockerfile, capas, construcción de imágenes |
| 4 | [4 - Optimizando imagenes.md](4%20-%20Optimizando%20imagenes.md) | Optimización de imágenes, dockerización de aplicaciones React |
| 5 | [5 - Almacenamiento.md](5%20-%20Almacenamiento.md) | Volúmenes, bind mounts, tmpfs, persistencia de datos |
| 6 | [6 - Registro.md](6%20-%20Registro.md) | Docker Hub, ECR y otros registros, push y pull de imágenes |
| 7 | [7 - Redes.md](7%20-%20Redes.md) | Redes de Docker, bridge, host, comunicación entre contenedores |
| 8 | [8 - Despliegue.md](8%20-%20Despliegue.md) | Ejemplos prácticos de despliegue (PostgreSQL, EC2, etc.) |

---

## Estructura del repositorio

```
curso-de-docker/
├── 1 - Introduccion.md
├── 2 - Imagenes y contenedores.md
├── 3 - Dockerfile.md
├── 4 - Optimizando imagenes.md
├── 5 - Almacenamiento.md
├── 6 - Registro.md
├── 7 - Redes.md
├── 8 - Despliegue.md
├── factorial/              # Ejemplo básico: cálculo de factorial
│   ├── Dockerfile
│   └── factorial.py
├── flaskapp/               # API web con Flask
│   ├── Dockerfile
│   ├── entrypoint.sh
│   ├── main.py
│   └── requirements.txt
├── reactapp/               # Aplicación React para optimización de imágenes
│   └── app/
└── img/                    # Diagramas e imágenes del curso
```

---

## Requisitos previos

- [Docker](https://docs.docker.com/get-docker/) instalado en tu sistema operativo
- Conocimientos básicos de línea de comandos
- (Opcional) Cuenta en [Docker Hub](https://hub.docker.com/) para el módulo de registro

Verifica tu instalación:

```sh
docker --version
docker run hello-world
```

## Cómo usar este repositorio

1. Clona el repositorio:

```sh
git clone https://github.com/MaxCloud101/curso-de-docker.git
cd curso-de-docker
```

2. Sigue los módulos en orden, del 1 al 8.
3. Ejecuta los ejemplos de cada sección en tu entorno local.
4. Consulta la carpeta `img/` para los diagramas referenciados en cada lección.

---

## Comunidad

Este curso forma parte de **Nación Cloud**, una comunidad hispanohablante enfocada en cloud computing, contenedores, AWS, Azure, GCP, CNCF, inteligencia artificial, data y desarrollo web.

---

## Licencia

Material educativo de uso libre para aprendizaje personal. Consulta el repositorio para más detalles sobre su distribución.
