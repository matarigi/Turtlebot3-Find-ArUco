from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [get_package_share_directory('turtlebot3_gazebo'), '/launch/turtlebot3_world.launch.py']
            ),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [get_package_share_directory('turtlebot3_bringup'), '/launch/rviz2.launch.py']
            ),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [get_package_share_directory('slam_toolbox'), '/launch/online_async_launch.py']
            ),
        ),
    ])