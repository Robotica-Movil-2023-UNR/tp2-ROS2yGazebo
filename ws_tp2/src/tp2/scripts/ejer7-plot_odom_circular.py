#!/usr/bin/env python3

import csv
import numpy as np
import matplotlib.pyplot as plt
import re

def main():
    odom_path = "ws_tp2/src/tp2/logs/log_circular.txt"
    odom_trajectory = []
    velos = []

    ## Parsear los datos del archivo log.txt
    try:
        with open(odom_path, 'r') as file:
            csv_reader = csv.reader(file, delimiter='\t')
            for row in csv_reader:
                # Obtengo los segundos y nanosegundos del string y armo el timestamp
                tmp = re.findall(r'\b\d+\b', row[0])
                row[0] = float(tmp[0]) + float(tmp[1])/1e9
                pose = np.array(row[0:4]).astype(float)
                odom_trajectory.append(pose)
                velos.append(np.array(row[4:6]).astype(float))

    except FileNotFoundError:
        print("File not found.", odom_path)
    except Exception as e:
        print("An error occurred:", e)

    # Para graficar necesito tener vectores columnas
    pose_tbl = np.array([pose[0:4] for pose in odom_trajectory])

    # Hago tiempo = 0 cuando arranca el registro de datos
    pose_tbl[:,0] = pose_tbl[:,0] - pose_tbl[0,0]

    # Camino del robot
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, aspect='equal')
    ax1.plot(pose_tbl[:,1], pose_tbl[:,2], 'b', label='Camino')
    ax1.legend()
    ax1.set_ylabel('Y [mts]')
    ax1.set_ylabel('X [mts]')
    ax1.grid()

    # Trayectoria o pose vs tiempo
    fig2, ax2 = plt.subplots(3, sharex='col')
    ax2[0].plot(pose_tbl[:,0], pose_tbl[:,1], 'b', label='pos x')
    ax2[1].plot(pose_tbl[:,0], pose_tbl[:,2], 'g', label='pos y')
    ax2[2].plot(pose_tbl[:,0], pose_tbl[:,3], 'r', label='yaw')

    fig2.suptitle('Trayectoria', fontsize=16)
    ax2[0].legend()
    ax2[0].set_ylabel('[mts]')
    ax2[0].grid()
    ax2[1].legend()
    ax2[1].set_ylabel('[mts]')
    ax2[1].grid()
    ax2[2].legend()
    ax2[2].set_ylabel('[rad]')
    ax2[2].grid()

    # Elegir 3 puntos y marcarlos en los graficos
    pos1 = 100
    pos2 = 800
    pos3 = 1400
    # Puntos en el camino del robot
    ax1.plot(pose_tbl[pos1,1], pose_tbl[pos1,2], 'xr')
    ax1.plot(pose_tbl[pos2,1], pose_tbl[pos2,2], 'xr')
    ax1.plot(pose_tbl[pos3,1], pose_tbl[pos3,2], 'xr')
    # Puntos en la trayectoria X
    ax2[0].plot(pose_tbl[pos1,0], pose_tbl[pos1,1], 'xr')
    ax2[0].plot(pose_tbl[pos2,0], pose_tbl[pos2,1], 'xr')
    ax2[0].plot(pose_tbl[pos3,0], pose_tbl[pos3,1], 'xr')
    # Puntos en la trayectoria Y 
    ax2[1].plot(pose_tbl[pos1,0], pose_tbl[pos1,2], 'xb')
    ax2[1].plot(pose_tbl[pos2,0], pose_tbl[pos2,2], 'xb')
    ax2[1].plot(pose_tbl[pos3,0], pose_tbl[pos3,2], 'xb')
    # Puntos en la trayectoria yaw
    ax2[2].plot(pose_tbl[pos1,0], pose_tbl[pos1,3], 'xg')
    ax2[2].plot(pose_tbl[pos2,0], pose_tbl[pos2,3], 'xg')
    ax2[2].plot(pose_tbl[pos3,0], pose_tbl[pos3,3], 'xg')
    
    # Punto a, el rango de X e Y y por qué

    # Punto b el rango de Yaw y por qué

    # Punto c. Diversos graficos con todas las posibilidades de signos de las velocidades
    # Indicar en el gráfico el sentido de avance del robot
    ## Parsear los datos del archivo log_cirXX.txt
    circ_path = ["ws_tp2/src/tp2/logs/log_cir1.txt",  "ws_tp2/src/tp2/logs/log_cir2.txt", "ws_tp2/src/tp2/logs/log_cir3.txt", "ws_tp2/src/tp2/logs/log_cir4.txt"]
    lista = []
    t = []
    x = []
    y = []
    
    fig5, axs5 = plt.subplots(2,2)
    # # fig.subplots_adjust(hspace = .5, wspace=.001)
    axs = axs5.ravel()
    axs[0].title.set_text('v+, w+')
    axs[1].title.set_text('v+, w-')
    axs[2].title.set_text('v-, w-')
    axs[3].title.set_text('v-, w+')
    # axs.set_aspect('equal')
    for a in axs5.flat:
        a.set_aspect('equal')

    for idx in range(len(circ_path)):
        with open(circ_path[idx], 'r') as file:
            csv_reader = csv.reader(file, delimiter='\t')
            for row in csv_reader:
                # Obtengo los segundos y nanosegundos del string y armo el timestamp
                tmp = re.findall(r'\b\d+\b', row[0])
                row[0] = float(tmp[0]) + float(tmp[1])/1e9
                t.append(row[0])
                x.append(float(row[1]))
                y.append(float(row[2]))
        # print(len(x))
        axs[idx].plot(x, y, 'b', label='Camino')
        # axs[idx].set_xlim(-10, 20)
        # axs[idx].set_ylim(-10, 20)
        lista.append([t, x, y])
        t=[]
        x=[]
        y=[]
        file.close()
        
    # Punto d. Describir la secuencia de comandos para que haga un cuadrado

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()        