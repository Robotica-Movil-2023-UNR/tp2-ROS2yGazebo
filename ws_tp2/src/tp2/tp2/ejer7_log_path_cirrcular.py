import rclpy
from rclpy.node import Node
import numpy as np

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose, Twist, Point


class Ejer7_Log(Node):

    def __init__(self):
        super().__init__('ejer7_log')

        self.twist_publisher = self.create_publisher(
            Twist,
            'cmd_vel',
            10)

        self.twist_publisher

    

def main(args=None):
    rclpy.init(args=args)

    ejer7_log = Ejer7_Log()

    rclpy.spin(ejer7_log)

    ejer7_log.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()