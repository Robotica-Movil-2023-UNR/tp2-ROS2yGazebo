# ROS2 + Gazebo

ROS2 y Simulador Gazebo configurado en entorno docker-compose + NoVNC. Permite usar un escritorio a través del navegador web. Sin aceleración de GPU 


## Dependencias
- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [Docker-compose](https://docs.docker.com/compose/install/)


## Pasos para ejecutar el contenedor
```bash
cd path/to/this/repo
docker-compose build
docker-compose up
```

## Pasos para acceder al escritorio
En un navegador web ir a la dirección [http://localhost:6080/](http://localhost:6080/) se debería ver una página como la siguiente (o presionar *Conectar*):
![NoVNC](./images/desktop.png)

Aquí se puede ejecutar programas normalmente como en un entorno de escritorio normal. Para abrir una terminal se puede usar el atajo de teclado `Ctrl + Alt + T` o hacer click en el icono de terminator en el escritorio.

## Pasos para desarrollo
El contenedor monta el directorio `./tp2` en el directorio `/home/catkin_ws/src` del contenedor. Por lo que se puede desarrollar normalmente en el directorio `./tp2` y los cambios se verán reflejados en el contenedor. Puede editar los archivos dentro de `./tp2` con su editor de texto favorito.

## Pasos para detener el contenedor
```bash
cd path/to/this/repo
docker-compose down
```