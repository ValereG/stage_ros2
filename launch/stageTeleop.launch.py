from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch.actions import IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    ld = LaunchDescription()

    included_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare("stage_ros2"), '/launch', '/stage.launch.py'])
    )

    myExecution = ExecuteProcess(
        cmd=['gnome-terminal', '--', 'ros2', 'run', 'turtlesim', 'turtle_teleop_key', '--ros-args', '-r', '__node:=teleop1', '-r', '/turtle1/cmd_vel:=/cmd_vel'],
        output='screen'
    )

    ld.add_action(included_launch)
    ld.add_action(myExecution)  
    return ld