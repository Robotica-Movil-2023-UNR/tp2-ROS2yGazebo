# FROM ros:humble-perception

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#     lsb-release \
#     wget \
#     gnupg \
#     ros-humble-turtlesim \
#     ros-humble-rqt* \
#     ros-humble-navigation2 \
#     ros-humble-nav2-bringup \
#     ros-humble-turtlebot3* \
#     ros-humble-gazebo-* \
#     ros-humble-demo-nodes-cpp \
#     ros-humble-demo-nodes-py && \
#     rm -rf /var/lib/apt/lists/*

# RUN ["/bin/bash", "-c", "source /opt/ros/humble/setup.bash"]

# WORKDIR /home/tp2/ws
# RUN mkdir /home/tp2/ws/src
# COPY ./entrypoint.sh /home/tp2/

# RUN chmod u+x /home/tp2/entrypoint.sh
# RUN ln -s /usr/bin/python3 /usr/bin/python

# ENTRYPOINT [ "/bin/bash", "-c", "/home/tp2/entrypoint.sh" ]

FROM osrf/ros:humble-desktop-full
ARG USERNAME=tp2
ARG USERID=1000
ARG HOME=/home/tp2
ENV DEBIAN_FRONTEND noninteractive

# Instalación nav2
# RUN apt update && apt upgrade -y && apt install -y \
RUN apt-get update && \
    apt-get install -y --no-install-recommends \        
      ros-$ROS_DISTRO-navigation2 \
      ros-$ROS_DISTRO-nav2-bringup \
      ros-humble-gazebo-* \
      ros-$ROS_DISTRO-turtlebot3*  \
      python3-pip \
      htop && \
      pip3 install transforms3d && \
      apt-get autoremove -y && \
      apt-get clean && \
      rm -rf /var/lib/apt/lists/*

RUN echo 'Crear usuario para no generar archivos como root'; \
    groupadd -f -g ${USERID} ${USERNAME}; \
    useradd -g ${USERID} -u ${USERID} -d ${HOME} -ms /bin/bash ${USERNAME}; \
    usermod -aG sudo ${USERNAME} ; \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers; \
    chown ${USERNAME}:${USERNAME} ${HOME}

USER ${USERNAME}:${USERNAME}

RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc
RUN echo "export TURTLEBOT3_MODEL=waffle" >> ~/.bashrc
RUN echo "export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/humble/share/turtlebot3_gazebo/models" >> ~/.bashrc
RUN echo "export PYTHONWARNINGS='ignore:setup.py install is deprecated::setuptools.command.install'"  >> ~/.bashrc

WORKDIR ${HOME}
