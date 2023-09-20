import rclpy
from rclpy.node import Node
import numpy as np

from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Pose, Twist
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray


class CylinderDetector(Node):

    def __init__(self):
        super().__init__('cylinder_detector')
        self.get_logger().info("CylinderDetector init")
        self.odom_subscriber = self.create_subscription(
            LaserScan,
            'scan',
            self.laser_callback,
            10)
        self.marker_publisher = self.create_publisher(MarkerArray, 'cylinders', 10)

    def laser_callback(self, msg):

        # 1. Detectar discontinuidades en el scan
        self.discontinuities_index = []
        for i in range(0, len(msg.ranges)-1):
            # Si hay un salto de más de 1 metro es una discontinuidad
            if np.abs(msg.ranges[i] - msg.ranges[i+1]) > 1:
                if msg.ranges[i] - msg.ranges[i+1] > 0:
                    # Para salto de +inf a numero finito
                    self.discontinuities_index.append(i+1)
                else:
                    # Para salto de numero finito a +inf
                    self.discontinuities_index.append(i)

        # 2. Determinar las poses x,y de los puntos de discontinuidad
        self.discontinuities_poses = []
        for i in self.discontinuities_index:
            angle = msg.angle_min + i * msg.angle_increment
            x = msg.ranges[i] * np.cos(angle)
            y = msg.ranges[i] * np.sin(angle)
            self.discontinuities_poses.append([x, y])

        # 3. Determinar el punto medio entre dos puntos de discontinuidad
        self.cylinder_poses = []
        for i in range(0, len(self.discontinuities_poses)-1, 2):
            x = (self.discontinuities_poses[i][0] + self.discontinuities_poses[i+1][0])/2
            y = (self.discontinuities_poses[i][1] + self.discontinuities_poses[i+1][1])/2
            self.cylinder_poses.append([x, y])
        
        # 4. Publicar los markers
        marker_array = self.generate_markerarray_message()
        self.marker_publisher.publish(marker_array)

    def generate_markerarray_message(self):
        marker_array = MarkerArray()
        for i in range(len(self.cylinder_poses)):
            self.get_logger().info("Cylinder pose: " + str(self.cylinder_poses[i]))
            marker = Marker()
            marker.header.frame_id = "base_link"
            marker.header.stamp = self.get_clock().now().to_msg()
            marker.id = i
            marker.type = marker.CYLINDER
            marker.action = marker.ADD
            marker.pose.position.x = self.cylinder_poses[i][0]
            marker.pose.position.y = self.cylinder_poses[i][1]
            marker.pose.position.z = 0.5
            marker.pose.orientation.x = 0.0
            marker.pose.orientation.y = 0.0
            marker.pose.orientation.z = 0.0
            marker.pose.orientation.w = 1.0
            marker.scale.x = 0.1
            marker.scale.y = 0.1
            marker.scale.z = 1.0
            marker.color.r = 0.0
            marker.color.g = 1.0
            marker.color.b = 0.0
            marker.color.a = 1.0
            marker_array.markers.append(marker)
        return marker_array


def main(args=None):
    rclpy.init(args=args)

    simple_controller = CylinderDetector()

    rclpy.spin(simple_controller)

    simple_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

