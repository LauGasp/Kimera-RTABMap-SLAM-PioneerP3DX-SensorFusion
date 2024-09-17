# Kimera-RTABMap-SLAM-PioneerP3DX-SensorFusion
This repository includes work from my dissertation, involving SLAM (Simultaneous Localization and Mapping) using a Pioneer P3DX robot equipped with a 2D LIDAR, Intel D435i and Mynt Eye sensors. The project integrates these sensors to provide accurate localization and mapping.

## Overview
The primary components and techniques used in this project include:
- **Robot:** Pioneer P3DX
- **Sensors:**
  - **2D LIDAR**
  - **Intel D435i**
  - **Mynt Eye**
 
**Tools/Packages:**

- **[rtabmap_ros](https://github.com/introlab/rtabmap_ros):** This ROS package provides the RTAB-Map framework for RGB-D SLAM using a global loop closure detector with real-time constraints. It can generate 3D point clouds of the environment and/or create a 2D occupancy grid map for navigation. In this project, it was used as a ground truth (GT) localization estimator.

- **[robot_localization](https://github.com/cra-ros-pkg/robot_localization):** A ROS package for nonlinear state estimation. The `ekf_robot_localization` node integrates data from multiple sensors using the Extended Kalman Filter (EKF) to enhance localization accuracy.

- **[hector_slam](https://github.com/tu-darmstadt-ros-pkg/hector_slam):** ROS package optimized for processing 2D LIDAR data and generating detailed 2D maps.

- **[Kimera-VIO-ROS](https://github.com/MIT-SPARK/Kimera-VIO-ROS):** A ROS wrapper for Kimera-VIO, providing Visual-Inertial Odometry (VIO) capabilities.

- **[Kimera-Semantics](https://github.com/MIT-SPARK/Kimera-Semantics):** Real-Time 3D Semantic Reconstruction from 2D data.

- **[Kimera-Multi](https://github.com/MIT-SPARK/Kimera-Multi):** This repository integrates multiple Kimera components, including Kimera-Semantics, Kimera-VIO, Kimera-Distributed, Kimera-Multi-LCD, Kimera-PGMO, DPGO, and DPGO-ROS. It provides a system designed for multiple robots with a distributed architecture.

- **[mmsegmentation_ros](https://github.com/jianhengLiu/mmsegmentation_ros):** A ROS package that utilizes the [mmsegmentation](https://github.com/open-mmlab/mmsegmentation) toolbox from OpenMMLab for semantic segmentation. In this case, the PSPNet network was used for detailed semantic segmentation.



## Setup and Usage

### 1. Docker Setup for RTAB-Map

The RTAB-Map setup is managed via Docker to handle dependencies and configurations. To start the RTAB-Map Docker container, use:

```bash
cd rtabmap_docker/docker
docker compose up

This command launches RTAB-Map with additional parameters and manages the odometry fusion. Specifically, it starts the rtabmap_slam and rtabmap_odom nodes, applies the Madgwick filter, and performs sensor fusion through the robot_localization package.


## **2. Launching the Robot and Sensors**

To launch the robot platform and the selected sensors, use the `catkin_pioneer` workspace. This command initializes the robot, the D435i camera, and the 2D LIDAR:

```bash
cd catkin_pioneer/
source devel/setup.bash
cd src/Pioneer_P3_DX2_packages_ROS_Noetic/Pioneer_P3_DX2_packages_ROS_Noetic/robot/launch
roslaunch robot robot.launch


The Mynt Eye sensor requires ROS Melodic. To set up the Mynt Eye sensor, use Docker to install the Mynt Eye SDK drivers. Run the following commands to start the Docker container for the Mynt Eye SDK:

cd mynt_docker/docker
docker compose up


