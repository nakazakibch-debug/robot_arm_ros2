# 🚀 Robot Arm Simulation (Gazebo & RViz)

This package contains the core simulation environment. It bridges the **SolidWorks** design with **ROS 2** and **Gazebo Sim** to allow for real-time control and visualization.

---

## 🛠️ Prerequisites & Installation
Before launching, make sure all required libraries and controller managers are installed. Run the following command in your terminal :

```bash
rosdep install -i --from-path src --rosdistro jazzy -y
```
If it doesn't work try manually install the required packages:
```bash
sudo apt install ros-jazzy-ros-gz \
                 ros-jazzy-gz-ros2-control \
                 ros-jazzy-ros-gz-sim \
                 ros-jazzy-ros-gz-bridge
```
```bash
sudo apt install ros-jazzy-ros2-control \
                 ros-jazzy-ros2-controllers \
                 ros-jazzy-controller-manager \
                 ros-jazzy-joint-state-broadcaster \
                 ros-jazzy-joint-trajectory-controller
```
```bash
sudo apt install ros-jazzy-xacro \
                 ros-jazzy-robot-state-publisher \
                 ros-jazzy-joint-state-publisher-gui
```
## 🏃 Execution Steps
To run the simulation and move the robot, follow these terminal commands in order:

### 1️⃣ Terminal 1: Launch Simulation
This command opens Gazebo and spawns the robot arm.
```bash
colcon build --packages-select robot_arm_simulation
source install/setup.bash
ros2 launch robot_arm_simulation sim.launch.py
```
### 2️⃣ Terminal 2: ROS-Gazebo Bridge & Controllers
Crucial Step: This starts the bridge that allows ROS 2 to communicate with Gazebo and activates the joint controllers.
```bash
source install/setup.bash
ros2 run ros_gz_bridge parameter_bridge /model/robot_arm/joint_trajectory@trajectory_msgs/msg/JointTrajectory@gz.msgs.JointTrajectory
```
### 3️⃣ Terminal 3: Robot Control GUI
This opens the "Sliders" window to manually move the joints.
```bash
source install/setup.bash
ros2 run rqt_joint_trajectory_controller rqt_joint_trajectory_controller
```
## 📂 File Structure Breakdown
| File/Folder | Purpose |
| :--- | :--- |
| **`config/arm_controllers.yaml`** | Defines the hardware controllers. |
| **`launch/sim.launch.py`** | Main launch script for Gazebo & RViz. |
| **`meshes/`** | STL files from SolidWorks. |
| **`urdf/robot_arm_urdf.xacro`** | Master robot description file. |
| **`CMakeLists.txt`** | Build instructions for Colcon. |
| **`package.xml`** | Project dependencies. |
