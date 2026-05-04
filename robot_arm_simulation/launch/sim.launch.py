import os
import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'robot_arm_simulation'
    
    xacro_file = os.path.join(get_package_share_directory(package_name), 'urdf', 'robot_arm_urdf.xacro')
    robot_description_raw = xacro.process_file(xacro_file).toxml()

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw, 'use_sim_time': True}]
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]),
        launch_arguments={'gz_args': '-r empty.sdf'}.items(),
    )

    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-topic', 'robot_description', '-name', 'robot_arm'],
        output='screen'
    )

    joint_state_broadcaster = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"]
    )

    arm_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["arm_controller"]
    )

    gripper_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["gripper_controller"]
    )

    return LaunchDescription([
        robot_state_publisher,
        gazebo,
        spawn_entity,
        joint_state_broadcaster,
        arm_controller,
        gripper_controller
    ])