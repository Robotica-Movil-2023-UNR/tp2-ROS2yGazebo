# Dado un archivo que contiene tiempo (timestamp), coordenadas x, y, orientación, velocidad lineal y angular separados
# por tabs, leer cada fila y graficar la trayectoria del robot en el plano xy.

import sys
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

if len(sys.argv) < 2:
    file_path = "../tp2/logs/log0.txt"
else:
    file_path = sys.argv[1]

try:
    file = open(file_path, "r")
    x = []
    y = []
    theta = []
    vx = []
    vz = []
    for line in file:
        fields = line.split("\t")
        fields = [float(field) for field in fields]
        x.append(fields[1])
        y.append(fields[2])
        theta.append(fields[3])
        vx.append(fields[4])
        vz.append(fields[5])

    fig=plt.figure()

    gs=GridSpec(4,2)
    gs.update(wspace=0.2, hspace=0.5)

    ax1=fig.add_subplot(gs[:,0]) 
    ax2=fig.add_subplot(gs[0,1])
    ax3=fig.add_subplot(gs[1,1])
    ax4=fig.add_subplot(gs[2,1])
    ax5=fig.add_subplot(gs[3,1])

    ax1.set_aspect('equal', adjustable='box')
    ax1.plot(x,y)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Camino seguido por el robot')

    ax2.plot(x)
    ax2.set_xlabel('t')
    ax2.set_ylabel('x[m]')
    ax2.grid()
    ax2.set_xticks(np.arange(0, len(x), 20))
    ax2.set_yticks(np.arange(min(x), max(x), 0.5))
    ax2.set_title('Posición x del robot respecto al tiempo')

    ax3.plot(y)
    ax3.set_xlabel('t')
    ax3.set_ylabel('y[m]')
    ax3.grid()
    ax3.set_xticks(np.arange(0, len(y), 20))
    ax3.set_yticks(np.arange(min(y), max(y), 0.5))
    ax3.set_title('Posición y del robot respecto al tiempo')

    ax4.plot(vx)
    ax4.set_xlabel('t')
    ax4.set_ylabel('vx')
    ax4.set_title('Velocidad lineal del robot respecto al tiempo')
    ax4.grid()
    ax4.set_xticks(np.arange(0, len(vx), 20))
    ax4.set_yticks(np.arange(min(vx)-1, max(vx)+1, 0.5))

    ax5.plot(vz)
    ax5.set_xlabel('t')
    ax5.set_ylabel('vz')
    ax5.set_title('Velocidad angular del robot respecto al tiempo')
    ax5.grid()
    ax5.set_xticks(np.arange(0, len(vz), 20))
    ax5.set_yticks(np.arange(min(vz)-1, max(vz)+1, 0.5))
    plt.show()

except FileNotFoundError:
    print("Error al abrir el archivo")
    sys.exit()