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

## Pasos para realizar pruebas
El contenedor monta el directorio `./tp2` en el directorio `/home/catkin_ws/src` del contenedor. Por lo que se puede desarrollar normalmente en el directorio `./tp2` y los cambios se verán reflejados en el contenedor. Puede editar los archivos dentro de `./tp2` con su editor de texto favorito.

Para todas las pruebas acontinuación, se utilizará la terinal `Terminator` que se encuentra en el escritorio.

### Ejercicio 7
Para ejecutar el controlador de posición del ejercicio 7, se debe ejecutar el siguiente comando en una terminal del contenedor:
```bash
# Lanzar la simulación:
ros2 launch tp2 tb3_simulation_launch
# En una nueva terminal (se puede dividir en horizontal la terminal actual) ejecutar:
ros2 run tp2 ejer7
```
El robot debería desplaarse en linea recta y luego girar en sentido anti horario. Para detener el programa presionar `Ctrl + C` en la terminal donde se ejecutó el programa.

### Ejercicio 8
Para ejecutar el algoritmo de deteccin ón de cilindros del ejercicio 8, se debe ejecutar el siguiente comando en una terminal del contenedor:
```bash
# Lanzar la simulación:
ros2 launch tp2 tb3_simulation_launch
# En una nueva terminal (se puede dividir en horizontal la terminal actual) ejecutar:
ros2 run tp2 ej8
```
En la ventana de rviz, configura el frame de referencia a `base_footprint` y agregar un tópico de tipo marker llamado `cylinders`. Se deberían ver cilindros de color verde en la simulación, los cuales corresponden a los obstáculos detectados en gazebo.
![Rviz](./images/ej8.png)

## Pasos para detener el contenedor
```bash
cd path/to/this/repo
docker-compose down
```