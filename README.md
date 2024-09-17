# Kimera-RTABMap-SLAM-PioneerP3DX-SensorFusion
This repository includes work from my dissertation, involving SLAM (Simultaneous Localization and Mapping) using a Pioneer P3DX robot equipped with a 2D LIDAR, Intel D435i and Mynt Eye sensors. The project integrates these sensors to provide accurate localization and mapping.

## Overview
The primary components and techniques used in this project include:
- **Robot:** Pioneer P3DX
- **Sensors:**
  - **2D LIDAR**
  - **Intel D435i**
  - **Mynt Eye**
 

**Software and Tools:**
  - **RTAB-Map:** Used for providing a ground truth (GT) localization estimate.
  - **EKF (Extended Kalman Filter):** `ekf_robot_localization` fuses data from different sensors to improve the estimation.
  - **Hector SLAM:** Used for 2D LIDAR data processing.
  - **Kimera:** Includes Kimera-VIO, Kimera-RPGO, and Kimera-Semantics.
  - **mmsegmentation_ros:** For semantic segmentation with PSPNet.
