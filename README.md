# Kimera-RTABMap-SLAM-PioneerP3DX-SensorFusion
This repository includes work from my dissertation, involving experimental tests with 3D SLAM (Simultaneous Localization and Mapping) methods using a robot equipped with multiple sensors. 

## Overview
The sensing system used include:
- **Robot:** Pioneer P3DX
- **Sensors:**
  - 2D LIDAR: Hokuyo URG-04L
  - RGBD camera: Intel RealSense D435i
  - Stereo Camera: Mynt Eye S1030



## Tools and Packages

1. **[rtabmap_ros](https://github.com/introlab/rtabmap_ros)**  
   **Purpose:** Real-time 3D SLAM and Localization  
   **Description:** This ROS package provides the RTAB-Map framework, which enables RGB-D SLAM (Simultaneous Localization and Mapping) with real-time global loop closure detection. It can generate 3D point clouds of the environment and/or produce a 2D occupancy grid map for navigation. In this project, RTAB-Map was utilized as a ground truth localization estimator.

2. **[robot_localization](https://github.com/cra-ros-pkg/robot_localization)**  
   **Purpose:** Nonlinear State Estimation using EKF  
   **Description:** The `ekf_robot_localization` node in this package fuses data from multiple sensors (e.g., IMU, GPS, odometry) using an Extended Kalman Filter (EKF). This can improve the accuracy of the robot's localization by combining different sensor modalities.

3. **[hector_slam](https://github.com/tu-darmstadt-ros-pkg/hector_slam)**  
   **Purpose:** 2D LIDAR SLAM  
   **Description:** Hector SLAM is optimized for processing 2D LIDAR data, allowing for the creation of high-resolution 2D maps in real time without needing odometry information.
   
5. **[Kimera-VIO-ROS](https://github.com/MIT-SPARK/Kimera-VIO-ROS)**  
   **Purpose:** Visual-Inertial Odometry (VIO)  
   **Description:** A ROS wrapper for Kimera-VIO, which performs Visual-Inertial Odometry by camera images and IMU data to estimate a robot’s trajectory. 

6. **[Kimera-RPGO](https://github.com/MIT-SPARK/Kimera-RPGO)**  
   **Purpose:** Pose Graph Optimization with Loop Closure  
   **Description:** Kimera-RPGO refines the pose estimates generated by Kimera-VIO. It adds support for loop-closure detection and pose-graph optimization.
   
8. **[Kimera-Semantics](https://github.com/MIT-SPARK/Kimera-Semantics)**  
   **Purpose:** Real-Time 3D Semantic Reconstruction  
   **Description:** Kimera-Semantics builds a 3D semantic map from 2D RGB-D data. It enhances spatial awareness by labeling objects in the environment (e.g., walls, floors, furniture), which is helpful for tasks such as navigation or object interaction.

9. **[Kalibr](https://github.com/ethz-asl/kalibr)**  
   **Purpose:** Calibration Tool for Sensors  
   **Description:** Kalibr is a calibration toolkit for visual-inertial and multi-camera systems. It was used in this project to perform the necessary calibrations for SLAM systems, particularly for Kimera.

10. **[Allan Variance ROS](https://github.com/ori-drs/allan_variance_ros)**  
   **Purpose:** Noise Modeling for IMU Sensors  
   **Description:** This package computes Allan variance, a method used to model the noise characteristics of inertial sensors (IMUs). 
11. **[Kimera-Multi](https://github.com/MIT-SPARK/Kimera-Multi)**  
   **Purpose:** Distributed SLAM for Multi-Robot Systems  
   **Description:** This repository integrates multiple Kimera components, including Kimera-Semantics, Kimera-VIO, Kimera-Distributed, Kimera-Multi-LCD, Kimera-PGMO, DPGO, and DPGO-ROS.
    
13. **[mmsegmentation_ros](https://github.com/jianhengLiu/mmsegmentation_ros)**  
    **Purpose:** Semantic Segmentation using Deep Learning  
    **Description:** This ROS package leverages the [mmsegmentation](https://github.com/open-mmlab/mmsegmentation) toolbox from OpenMMLab for real-time semantic segmentation. In this project, the PSPNet network was employed for detailed semantic segmentation, providing pixel-level classifications of the environment.





## Setup and Usage

### 1. Launching the Robot and Sensors

To launch the robot platform and the selected sensors, use the `catkin_pioneer` workspace. This command initializes the robot, the D435i camera, and the 2D LIDAR:


```
roslaunch robot robot.launch 
```
To control the robot via keyboard inputs, start the teleop node using the following command:
```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```
Note: Grant necessary permissions to access the USB port for the robot:
```
sudo chmod 777 -R /dev/ttyUSB0
```

The Mynt Eye sensor requires ROS Melodic. To set up the Mynt Eye sensor, use Docker to install the Mynt Eye SDK drivers. Run the following commands to start the Docker container for the Mynt Eye SDK:
```
cd mynteye_docker/docker
docker compose up
```
### 2. Docker Setup for RTAB-Map and Robot localization 

The RTAB-Map setup is managed via Docker to handle dependencies and configurations. To start the RTAB-Map Docker container, use:

```
cd rtabmap_docker/docker
docker compose up
```

This command launches RTAB-Map with additional parameters and manages the odometry fusion. Specifically, it starts the `rtabmap_odom node`, `rtabmap_slam node`, `imu_filter_node` and `ekf_localization_node`.

### 3. Hector SLAM for 2D LIDAR

For processing 2D LIDAR data with Hector SLAM, a script named `pose_to_odom_hectorslam.py` is available in the `/Other_code` directory. This script converts odometry data to pose and serves as input for robot localization package.

To run Hector SLAM, use:
```
roslaunch hector_slam_launch tutorial.launch
```

### 4. Kimera for single robots


This method includes several modules: **Kimera-VIO**, **Kimera-RPGO**, and **Kimera-Semantics**. Below are the steps to get these modules running on a single robot.

#### Running the Kimera Docker Container

The `docker pull laugasp/kimera_workspace:latest` is used to download the Docker image used. 

```
cd Docker/kimera_docker/docker 
docker start kimera_container
docker exec -it kimera_container /bin/bash
```

To get the single robot odometry working, ensure that: the topics are mapped correctly and that you are pointing to the right folder that has your robot's and sensor's configurations. 

Once configured, you can launch VIO on each robot, input stereo images and IMU data, and get a reasonable odometry estimate. Here's how to launch Kimera-VIO:
```
cd /home/catkin_ws/src/Kimera-VIO-ROS/launch
roslaunch kimera_vio_ros kimera_vio_ros_realsense_new.launch 
```
Note: Other launch files are available, such as those provided by the Kimera authors for the Euroc dataset.

To change calibration parameters:
``` cd /home/catkin_ws/src/Kimera-VIO/params ```

Kimera-Semantics requires odometry data and a neural network for segmentation. For this, the `mmsegmentation_ros` package is adapted for class filtering and is based on the mmsegmentation framework.
Kimera-Semantics can be fed with data from other odometry systems, such as Kimera-VIO, Kimera-RPGO, or RTAB-Map.

To run Kimera-Semantics: 

``` cd /home/catkin_ws/src/Kimera-Semantics/kimera_semantics_ros ```

Make sure to input the correct sensor frames and topics. There is a folder with launch files and `.csv` files in the `/cfg` directory containing the correct semantic-color configurations. 

Example of launching Kimera-Semantics:
```roslaunch kimera_semantics_ros kimera_metric_realsense_new.launch```

### 5. Docker with mmsegmentation ROS Container

To start the **mmsegmentation_ros** Docker container, run the following commands:

```
cd mmseg_ros_docker/docker
docker start docker-mmsegmetation-melodic-1
# or use the container ID:
docker start 1f9e8304ccdc
docker exec -it 1f9e8304ccdc /bin/bash

```
**Semantic Segmentation with mmsegmentation_ros**

The mmsegmentation_ros package contains the `mmsegmentor.py` script created by Jianheng Liu. This script performs semantic segmentation on images received from a ROS topic, applying a pre-trained segmentation model, and then publishing the processed results.

Key parameters loaded in the script include:

    - config_path: Path to the model configuration file.
    - checkpoint_path: Path to the pre-trained model weights.
    - device: Specifies the CPU or GPU for inference.
    - palette: Color palette used for visualizing the segmentation maps.
    - publish_rate: Rate at which the processed images are published.

**Custom Script for Class Filtering**

Building on top of the original script, a custom script was added that allows loading a `.yaml` file to filter specific classes from the chosen dataset and select the desired color palette for segmentation.

Note: The color format for output images is BGR. 

Ensure that the paths and parameters in the launch file are correctly set to match your dataset and configuration. The launch file will handle calling the node and passing the required parameters.

**Model Configurations and Datasets**

In this experiment, the PSPNet network with an R-50-D8 backbone was used. It was trained on the ADE20K dataset, but the Cityscapes dataset was also tested.

You can find other models and results available for different datasets [here](https://github.com/open-mmlab/mmsegmentation/tree/main/configs). 

To run the models, you will need both the `config` file and the `model` (`checkpoint`) file.

### 6. Docker Evaluation and NVIDIA GPU Monitoring

#### Docker Container Usage Monitoring

In the `/Other_code` directory, there is a script to monitor Docker container usage (CPU and Memory) and generate plots in a PDF document.

To record the resource usage data (CPU and Memory) of your Docker container:

1. Edit the container name and the `.bag` file that will be played in the `python run_docker_down_csv.py` file.

   This will generate a CSV file with the recorded container data.

2. Once you have the CSV data, generate a plot and export it to a PDF file by running: ```python plot_docker_usage.py```

   This will create a PDF file with CPU and memory usage plotted over time.

#### GPU Utilization Monitoring and Plot Generation

To monitor GPU and memory usage over time, the `nvidia-smi` command is used. 

1. Use the appropriate script to capture GPU metrics.
2. The script will generate a plot that is saved as a PDF document.   ```python plot_gpu_usage.py```




