# 🧠 Robot Arm MoveIt Config

This package contains the **MoveIt 2** configuration for the robot arm. It enables advanced features like **Inverse Kinematics (IK)**, **Collision Checking**, and **Motion Planning**.

---

## 🛠️ Installation & Setup
Ensure you have the MoveIt 2 binaries installed for ROS 2 Jazzy:

```bash
sudo apt update
sudo apt install ros-jazzy-moveit \
                 ros-jazzy-moveit-configs-utils \
                 ros-jazzy-moveit-setup-assistant \
                 ros-jazzy-moveit-ros-visualization \
                 ros-jazzy-moveit-ros-move-group
```
## 🏃 How to Run
### 1️⃣ Option A: Launching the MoveIt Demo
This will open RViz with the MoveIt panel, allowing you to drag the robot's end-effector and plan paths in a virtual environment.
```bash
colcon build --packages-select robot_arm_config
source install/setup.bash
ros2 launch robot_arm_config demo.launch.py
```
### 2️⃣ Option B: MoveIt Setup Assistant
If you need to modify joints, self-collisions, or planning groups, use the Setup Assistant:
```bash
ros2 launch moveit_setup_assistant setup_assistant.launch.py
```
## 📂 Configuration Details
| File/Folder | Purpose |
| :--- | :--- |
| **`config/kinematics.yaml`** | Defines the IK solver and search resolution for the arm. |
| **`config/joint_limits.yaml`** | Specifies velocity, acceleration, and position limits for each joint. |
| **`config/initial_positions.yaml`** | Sets the default starting posture for the robot in MoveIt. |
| **`config/moveit_controllers.yaml`** | Bridges MoveIt with the hardware/simulation controllers. |
| **`config/robot_arm.srdf`** | Semantic Robot Description (defines groups, poses, and collisions). |
| **`launch/demo.launch.py`** | Main entry point to test MoveIt planning in RViz without Gazebo. |
| **`launch/move_group.launch.py`** | Starts the core MoveIt node responsible for motion planning. |
| **`launch/moveit_rviz.launch.py`** | Launches RViz pre-configured with the MoveIt Motion Planning plugin. |
| **`launch/rsp.launch.py`** | Standard robot_state_publisher for the MoveIt context. |
| **`CMakeLists.txt`** | Build configuration for the ROS 2 environment. |
