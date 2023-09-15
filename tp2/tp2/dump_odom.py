#!/usr/bin/env python3

"""
ROS node for 2D odometry dump
"""

import sys
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion

class DumpOdom(Node):
    """ Node class """
    def __init__(self):
        super().__init__('dump_odom')

        # Node subscribers
        self.subscription = self.create_subscription(Odometry, '/odom', self.odom_cb, 10)
        self.subscription

    def odom_cb(self, msg):
        """ Odometry subscriber callback """
        quat = msg.pose.pose.orientation
        orientation_list = [quat.x, quat.y, quat.z, quat.w]
        (_, _, yaw) = euler_from_quaternion(orientation_list)

        print(str(msg.header.stamp.sec+msg.header.stamp.nanosec/1000000000) + '\t' + \
        str(msg.pose.pose.position.x) + '\t' + \
        str(msg.pose.pose.position.y) + '\t' + str(yaw) + '\t' + \
        str(msg.twist.twist.linear.x) + '\t' + \
        str(msg.twist.twist.angular.z))


def main(args=None):
    rclpy.init(args=args)
    node = DumpOdom()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
