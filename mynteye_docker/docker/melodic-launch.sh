#!/bin/bash
set -e

#Build the catkin workspace
cd /root/catkin_ws
catkin config --extend /root/MYNT-EYE-S-SDK/wrappers/ros/devel --whitelist $BUILDLIST #only builds these packages
catkin build -v
source $SETUP

roslaunch --wait $ROSPACKAGE $LAUNCHFILE #launch the file
