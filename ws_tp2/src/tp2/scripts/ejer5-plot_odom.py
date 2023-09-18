#!/usr/bin/env python3

import csv
import numpy as np
import matplotlib.pyplot as plt
import re

def main():
    odom_path = "./src/log.txt"
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
    velo_tbl = np.array([velo[0:2] for velo in velos])

    # Punto a, el camino del robot
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, aspect='equal')
    ax1.plot(pose_tbl[:,1], pose_tbl[:,2], 'b', label='Camino')
    ax1.legend()
    ax1.set_ylabel('Y [mts]')
    ax1.set_ylabel('X [mts]')
    ax1.grid()

    # Punto b, trayectoria o pose vs tiempo
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

    # Punto c, velocidades vs tiempo
    fig3, ax3 = plt.subplots(2, sharex='col')
    ax3[0].plot(pose_tbl[:,0], velo_tbl[:,0], 'b', label='Vel. X')
    ax3[1].plot(pose_tbl[:,0], velo_tbl[:,1], 'g', label='Vel. Y')

    fig3.suptitle('Velocidades', fontsize=16)
    ax3[0].legend()
    ax3[0].set_ylabel('[mts/seg]')
    ax3[0].grid()
    ax3[1].legend()
    ax3[1].set_ylabel('[mts/seg]')
    ax3[1].grid()

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()        