from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("robot_arm", package_name="robot_arm_config")
        .robot_description(file_path="config/robot_arm.urdf.xacro")
        .to_moveit_configs()
    )
    return generate_demo_launch(moveit_config)