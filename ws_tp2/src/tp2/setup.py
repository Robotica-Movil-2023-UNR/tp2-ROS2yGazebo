from setuptools import find_packages, setup

package_name = 'tp2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='elgarbe',
    maintainer_email='leogarberoglio@hotmail',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ejer7_log_path_cirrcular = tp2.ejer7_log_path_cirrcular:main'
        ],
    },
)
