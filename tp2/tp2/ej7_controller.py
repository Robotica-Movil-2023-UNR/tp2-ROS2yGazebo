import rclpy
from rclpy.node import Node
import numpy as np

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose, Twist, Point


class SimpleController(Node):

    def __init__(self):
        super().__init__('simple_controller')
        self.odom_subscriber = self.create_subscription(
            Odometry,
            'odom',
            self.odom_callback,
            10)
        self.twist_publisher = self.create_publisher(
            Twist,
            'cmd_vel',
            10)

        self.odom_subscriber
        self.twist_publisher
        self.state = 0
        self.initial_pose_initialized = False
        self.prev_pose = Pose()

    def odom_callback(self, msg):
        if self.initial_pose_initialized == False:
            self.prev_pose = msg.pose.pose
            self.initial_pose_initialized = True
            return

        # self.get_logger().info('Current  target: ' + str(self.target_pose.position.x) +
                            #    ', ' + str(self.target_pose.position.y))

        if self.state == 0:
            go_forward = Twist()
            go_forward.linear.x = 0.5
            self.twist_publisher.publish(go_forward)
        elif self.state == 1:
            turn_left = Twist()
            turn_left.angular.z = 0.1
            self.twist_publisher.publish(turn_left)

        if self.state == 0:
            distance = self.distance(msg.pose.pose, self.prev_pose)
            self.get_logger().info("distance diff:" + str(distance))
            if distance > 2.0:
                self.get_logger().info('Target reached')
                self.state = 1
        elif self.state == 1:
            prev_yaw = self.yaw_from_quaternion(self.prev_pose.orientation)
            current_yaw = self.yaw_from_quaternion(msg.pose.pose.orientation)
            if current_yaw < 0:
                current_yaw = -current_yaw
                current_yaw = current_yaw + 180
            distance = np.abs((prev_yaw+90) - current_yaw)
            self.get_logger().info("angle diff:" + str(distance))
            if distance < 0.2:
                self.prev_pose = msg.pose.pose
                self.get_logger().info('Target reached')
                self.state = 0

    def distance(self, pose1, pose2):
        return ((pose1.position.x - pose2.position.x)**2 + (pose1.position.y - pose2.position.y)**2)**(1/2)
    
    def yaw_from_quaternion(self, quaternion):
        x = quaternion.x
        y = quaternion.y
        z = quaternion.z
        w = quaternion.w

        # Calculate roll (x-axis rotation)
        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)

        # Calculate pitch (y-axis rotation)
        sinp = 2 * (w * y - z * x)
        if np.abs(sinp) >= 1:
            pitch = np.sign(sinp) * np.pi / 2  # Use 90 degrees if out of range
        else:
            pitch = np.arcsin(sinp)

        # Calculate yaw (z-axis rotation)
        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        yaw = np.arctan2(siny_cosp, cosy_cosp)

        yaw = yaw * 180 / np.pi

        return yaw


def main(args=None):
    rclpy.init(args=args)

    simple_controller = SimpleController()

    rclpy.spin(simple_controller)

    simple_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
