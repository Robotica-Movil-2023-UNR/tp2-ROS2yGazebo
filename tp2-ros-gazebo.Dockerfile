FROM tiryoh/ros2-desktop-vnc:humble

RUN apt-get update && apt-get install -y \
      ros-humble-turtlebot3* \
      ros-humble-nav2-bringup \
      ros-humble-tf-transformations \
      && pip3 install transforms3d \
      && rm -rf /var/lib/apt/lists/*

WORKDIR /home/ubuntu/catkin_ws
RUN mkdir /home/ubuntu/catkin_ws/src
COPY ./entrypoint.sh /home/ubuntu/

RUN chmod u+x /home/ubuntu/entrypoint.sh
RUN ln -s /usr/bin/python3 /usr/bin/python

ENTRYPOINT [ "/bin/bash", "-c", "/home/ubuntu/entrypoint.sh" ]
