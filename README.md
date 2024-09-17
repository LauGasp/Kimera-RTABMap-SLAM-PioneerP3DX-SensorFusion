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

- **[rtabmap_ros](https://github.com/introlab/rtabmap_ros):** This ROS package provides the RTAB-Map framework for RGB-D SLAM. It offers a ground truth (GT) localization estimate through a global loop closure detector with real-time constraints. It can generate 3D point clouds of the environment and/or create a 2D occupancy grid map for navigation.

- **[robot_localization](https://github.com/cra-ros-pkg/robot_localization):** A ROS package for nonlinear state estimation. The `ekf_robot_localization` node integrates data from multiple sensors using the Extended Kalman Filter (EKF) to enhance localization accuracy.

- **[hector_slam](https://github.com/tu-darmstadt-ros-pkg/hector_slam):** ROS package optimized for processing 2D LIDAR data and generating detailed 2D maps.

- **[Kimera-VIO-ROS](https://github.com/MIT-SPARK/Kimera-VIO-ROS):** A ROS wrapper for Kimera-VIO, providing Visual-Inertial Odometry (VIO) capabilities.

- **[Kimera-Semantics](https://github.com/MIT-SPARK/Kimera-Semantics):** Real-Time 3D Semantic Reconstruction from 2D data.

- **[Kimera-Multi](https://github.com/MIT-SPARK/Kimera-Multi):** This repository integrates multiple Kimera components, including Kimera-Semantics, Kimera-VIO, Kimera-Distributed, Kimera-Multi-LCD, Kimera-PGMO, DPGO, and DPGO-ROS.

- **[mmsegmentation_ros](https://github.com/open-mmlab/mmsegmentation_ros):** A ROS package that utilizes the mmsegmentation toolbox from OpenMMLab for semantic segmentation. In this case, the PSPNet network was used for detailed semantic segmentation.

