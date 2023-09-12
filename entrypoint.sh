#!/bin/bash
# set -e

# # setup ros environment
# source /usr/share/gazebo/setup.sh
source "/opt/ros/${ROS_DISTRO}/setup.bash"

exec "$@"

# Create User
# USER=${USER:-root}
# HOME=/root
# if [ "$USER" != "root" ]; then
#     echo "* enable custom user: $USER"
#     useradd --create-home --shell /bin/bash --user-group --groups adm,sudo $USER
#     echo "$USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
#     if [ -z "$PASSWORD" ]; then
#         echo "  set default password to \"tp2\""
#         PASSWORD=tp2
#     fi
#     HOME=/home/$USER
#     echo "$USER:$PASSWORD" | /usr/sbin/chpasswd 2> /dev/null || echo ""
#     cp -r /root/{.config,.gtkrc-2.0,.asoundrc} ${HOME} 2>/dev/null
#     chown -R $USER:$USER ${HOME}
#     [ -d "/dev/snd" ] && chgrp -R adm /dev/snd
# fi

# colcon
# BASHRC_PATH=$HOME/.bashrc
# grep -F "source /opt/ros/$ROS_DISTRO/setup.bash" $BASHRC_PATH || echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> $BASHRC_PATH
# grep -F "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" $BASHRC_PATH || echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> $BASHRC_PATH
# chown $USER:$USER $BASHRC_PATH
