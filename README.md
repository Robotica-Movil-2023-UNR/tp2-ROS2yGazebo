# tp2-ROS2yGazebo

## Pasos para ejecutar el contenedor
```bash
cd path/to/this/repo
docker compose build
docker compose up -d
```
Con este comando se levanta la imagen en modo detached liberando la terminal donde se ejecutó el comando. Confirmar la creación de la imagen con

```bash
docker ps
```

## Pasos para realizar pruebas
El contenedor monta el directorio `ws_tp2` en el directorio `/` del contenedor. Por lo que se puede desarrollar normalmente en el directorio `ws_tp2` y los cambios se verán reflejados en el contenedor.
Para obtener una consola dentro de la imágen ejecutar:

```bash
docker exec  -it tp2-ros2ygazebo-tp2-1 bash
```

A continuación se muestran los comandos a ejecutar para cada ejercicio. Dichos comandos se deberán correr en consolas del contenedor
### Ejercicio 4
Para obtener el registro (log) de odometría del robot, se debe ejecutar el siguiente comando en una terminal del contenedor:
```bash
# Lanzar la simulación:
ros2 launch tp2 tb3_simulation_launch
# En una nueva terminal ejecutar:
ros2 run teleop_twist_keyboard teleop_twist_keyboard
# En una nueva terminal ejecutar:
ros2 run tp2 dump_odom
```
Se imprimirá en pantalla los valores de la odometría del robot a medida que se mueve el mismo.

### Ejercicio 5, 6 y 7
Se hace uso de los scripts en la carpta tp2/scripts y los logs en tp2/logs. Dichos scripts pueden ser usados tanto dentro como fuera del contenedor
```bash
cd ws_tp/src/tp2/scripts
python3 ejer5-plot_odom.py
python3 ejer6-plot_odom_circular.py
python3 ejer7-plot_odom_circular.py
```


### Ejercicio 8
Para ejecutar el algoritmo de deteccin ón de cilindros del ejercicio 8, se debe ejecutar el siguiente comando en una terminal del contenedor:
```bash
# Lanzar la simulación:
ros2 launch tp2 tb3_simulation_launch
# En una nueva terminal ejecutar:
ros2 run tp2 ej8
```
En la ventana de rviz, configura el frame de referencia a `base_footprint` y agregar un tópico de tipo marker llamado `cylinders`. Se deberían ver cilindros de color verde en la simulación, los cuales corresponden a los obstáculos detectados en gazebo.

