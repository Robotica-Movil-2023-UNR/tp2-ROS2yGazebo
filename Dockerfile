ARG ROS_DISTRO=humble

FROM osrf/ros:$ROS_DISTRO-desktop-full

RUN apt-get update && apt-get install -y \
      ros-humble-turtlebot3* \
      ros-humble-nav2-bringup \
      && rm -rf /var/lib/apt/lists/*

RUN ["/bin/bash", "-c", "source /opt/ros/humble/setup.bash"]

# WORKDIR /home/tp2/ws
# RUN mkdir /home/tp2/ws/src
# COPY ./entrypoint.sh /home/tp2/

# RUN chmod u+x /home/tp2/entrypoint.sh
# RUN ln -s /usr/bin/python3 /usr/bin/python

# ENTRYPOINT [ "/bin/bash", "-c", "/home/tp2/entrypoint.sh" ]

# # ARG USERNAME=tp2
# # ARG USERID=1000
# ARG HOME=/home/tp2
# ENV DEBIAN_FRONTEND noninteractive

# # Instalación nav2
# RUN apt update && apt upgrade -y && apt install -y \
#         ros-$ROS_DISTRO-turtlesim \
#         ros-$ROS_DISTRO-rqt* \
#         ros-$ROS_DISTRO-navigation2 \
#         ros-$ROS_DISTRO-nav2-bringup \
#         ros-$ROS_DISTRO-turtlebot3* \
#         ros-$ROS_DISTRO-gazebo-* \
#         ros-$ROS_DISTRO-pointcloud-to-laserscan && \
#     apt-get autoremove -y && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# # RUN echo 'Crear usuario para no generar archivos como root'; \
# #     groupadd -f -g ${USERID} ${USERNAME}; \
# #     useradd -g ${USERID} -u ${USERID} -d ${HOME} -ms /bin/bash ${USERNAME}; \
# #     usermod -aG sudo ${USERNAME} ; \
# #     echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc

# # USER ${USERNAME}:${USERNAME}

# WORKDIR ${HOME}
