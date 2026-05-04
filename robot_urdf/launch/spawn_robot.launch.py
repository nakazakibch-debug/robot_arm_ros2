import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, AppendEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # 1. تحديد مسارات الحزم
    pkg_ros_gz_sim = FindPackageShare('ros_gz_sim').find('ros_gz_sim')
    pkg_robot_urdf = FindPackageShare('robot_urdf').find('robot_urdf')
    
    # 2. تحديد مسار ملف الـ URDF
    urdf_file_path = os.path.join(pkg_robot_urdf, 'urdf', 'RobotURDF.urdf')

    # --- الحل الجذري للأخطاء يبدأ هنا ---
    
    # قراءة محتوى الملف كنص (لحل مشكلة robot_state_publisher)
    with open(urdf_file_path, 'r') as infp:
        robot_desc = infp.read()

    # استبدال الجملة الوهمية بالمسار الحقيقي (لحل مشكلة انهيار Gazebo)
    robot_desc = robot_desc.replace(
        '$(find robot_urdf)',
        pkg_robot_urdf
    )
    
    # -----------------------------------

    # 3. إعداد مسارات الـ Plugins والـ Meshes
    set_env_var_plugin = AppendEnvironmentVariable(
        'GZ_SIM_SYSTEM_PLUGIN_PATH',
        '/opt/ros/jazzy/lib'
    )
    
    set_env_var_resource = AppendEnvironmentVariable(
        'GZ_SIM_RESOURCE_PATH',
        os.path.join(pkg_robot_urdf, '..')
    )

    return LaunchDescription([
        set_env_var_plugin,
        set_env_var_resource,

        # 4. تشغيل Gazebo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
            )
        ),

        # 5. تشغيل Robot State Publisher (تم تغيير urdf_file إلى robot_desc)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}]
        ),

        # 6. وضع الروبوت في المحاكي (استخدام -string بدلاً من -file)
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=['-string', robot_desc, '-name', 'my_robot'],
            output='screen'
        )
    ])