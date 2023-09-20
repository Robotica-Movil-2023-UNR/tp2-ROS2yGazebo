from setuptools import find_packages, setup

package_name = 'tp2'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/tb3_simulation_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Martin Nievas',
    maintainer_email='devel@martinnievas.ar',
    description='TP2: ROS2 y Simulador Gazebo<',
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ej5 = tp2.ej5:main',
            'dump_odom = tp2.dump_odom:main',
            'ej7_controller = tp2.ej7_controller:main'
        ],
    },
)
