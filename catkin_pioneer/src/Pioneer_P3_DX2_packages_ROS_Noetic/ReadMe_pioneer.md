# Pioneer Package

This is the package for the Pioneer robot, facilitated by Prof. Dr. Rui P. Rocha. The package was provided with most components organized, which facilitated integration and use.

## Recent Modifications

An important modification has been made to improve the package's functionality:

- Enabled the ability to enable/disable the publication of the odometry TF, which can sometimes conflict with other systems (in this case, with `ekf_robot_localization`).

- Updated the code to use `tf2_ros`. `tf2` provides improvements over `tf`. 





# DATA RECORDING:

# 1. Start cameras - Mynt Eye
# Navigate to the Mynt Eye Docker directory and start the Mynt Eye cameras using Docker Compose
cd Docker/mynteye_docker/docker 
docker compose up

# 2. Start the robot and other sensors (D435i and LIDAR)
# Grant necessary permissions to access the USB port for the robot
sudo chmod 777 -R /dev/ttyUSB0
# Launch the robot along with the associated sensors using a ROS launch file
roslaunch robot robot.launch 

# 3. Control the robot using a keyboard
# Start the teleop node to control the robot via keyboard inputs
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
# If using Gazebo or a different command topic, specify it with the 'cmd_vel' argument
rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/Pionner/cmd_vel 

# 4. Record data
# Start recording data into a ROS bag
rosbag record -b 8192 /cmd_vel /odom_wheels /realsense/aligned_depth_to_color/camera_info /realsense/aligned_depth_to_color/image_raw /realsense/color/camera_info /realsense/color/image_raw  /realsense/depth/image_rect_raw /realsense/depth/camera_info /realsense/imu /realsense/gyro/imu_info /realsense/infra1/camera_info /realsense/infra1/image_rect_raw /realsense/infra2/camera_info /realsense/infra2/image_rect_raw /tf /tf_static /scan /laser_status /mynteye/depth/image_raw /mynteye/depth/camera_info /mynteye/imu/data_raw /mynteye/left_rect/camera_info /mynteye/right_rect/camera_info /mynteye/left_rect/image_rect /mynteye/right_rect/image_rect


