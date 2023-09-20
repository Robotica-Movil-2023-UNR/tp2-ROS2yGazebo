# Dado un archivo que contiene tiempo (timestamp), coordenadas x, y, orientación, velocidad lineal y angular separados
# por tabs, leer cada fila y graficar la trayectoria del robot en el plano xy.

import sys
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

if len(sys.argv) < 2:
    file_path = "../tp2/logs/log_ej7_nn.txt"
else:
    file_path = sys.argv[1]

try:
    file = open(file_path, "r")
    t = []
    x = []
    y = []
    theta = []
    vx = []
    vz = []
    for line in file:
        fields = line.split("\t")
        fields = [float(field) for field in fields]
        t.append(fields[0])
        x.append(fields[1])
        y.append(fields[2])
        theta.append(fields[3])
        vx.append(fields[4])
        vz.append(fields[5])

    fig=plt.figure()

    initial_time = t[0]
    new_t = [round(float(time-initial_time),2) for time in t]

    gs=GridSpec(3,2)
    gs.update(wspace=0.2, hspace=0.5)

    ax1=fig.add_subplot(gs[:,0]) 
    ax2=fig.add_subplot(gs[0,1])
    ax3=fig.add_subplot(gs[1,1])
    ax4=fig.add_subplot(gs[2,1])
    delta_t = 80

    ax1.set_aspect('equal', adjustable='box')
    ax1.plot(x,y)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.grid()
    ax1.set_xticks(np.arange(min(x), max(x) + 0.5, 0.25))
    ax1.set_yticks(np.arange(min(y), max(y) + 0.5, 0.25))
    ax1.set_title('Camino seguido por el robot')

    ax2.plot(new_t, x)
    ax2.set_xlabel('t')
    ax2.set_ylabel('x[m]')
    ax2.grid()
    ax2.set_yticks(np.arange(min(x), max(x), 0.5))
    ax2.set_title('Posición x del robot respecto al tiempo')

    ax3.plot(new_t, y)
    ax3.set_xlabel('t')
    ax3.set_ylabel('y[m]')
    ax3.grid()
    ax3.set_yticks(np.arange(min(y), max(y), 0.5))
    ax3.set_title('Posición y del robot respecto al tiempo')

    ax4.plot(new_t, theta)
    ax4.set_xlabel('t')
    ax4.set_ylabel('theta')
    ax4.set_title('Orientación del robot respecto al tiempo')
    ax4.grid()
    ax4.set_yticks(np.arange(min(theta)-1, max(theta)+1, 1.))

    timestamp_markers = [len(new_t)//5, len(new_t)//2, 2*len(new_t)//3]
    colors = ['red', 'green', 'blue']
    for timestamp,color in zip(timestamp_markers, colors):
        ax1.plot(x[timestamp], y[timestamp], marker=(3, 0, -90+theta[timestamp]*180/np.pi), linestyle='None', markersize=20, color=color)
        ax2.plot(new_t[timestamp], x[timestamp], 'o', color=color)
        ax3.plot(new_t[timestamp], y[timestamp], 'o', color=color)
        ax4.plot(new_t[timestamp], theta[timestamp], 'o', color=color)

    plt.show()

except FileNotFoundError:
    print("Error al abrir el archivo")
    sys.exit()
