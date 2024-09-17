FROM osrf/ros:noetic-desktop-full

ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_WS=/home/catkin_ws


# For 20.04 (noetic)
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y \
      cmake git build-essential unzip pkg-config autoconf \
      libboost-all-dev \
      libjpeg-dev libpng-dev libtiff-dev \
      libvtk7-dev libgtk-3-dev \
      libatlas-base-dev gfortran \
      libparmetis-dev \
      libtbb-dev \
      python3-wstool python3-catkin-tools

RUN apt-get update && apt-get install \
	ros-$ROS_DISTRO-image-geometry \
	ros-$ROS_DISTRO-pcl-ros \
	ros-$ROS_DISTRO-cv-bridge

# Install GTSAM (a non ROS dependency)
RUN apt-get update \
  && apt install -y software-properties-common \
  && add-apt-repository -y ppa:borglab/gtsam-release-4.0 \
  && apt-get update \
  && apt install -y libgtsam-dev libgtsam-unstable-dev
  #&& rm -rf /var/lib/apt/lists/*


#Install Kimera VIO ROS
WORKDIR $ROS_WS
RUN mkdir src && catkin init

SHELL ["/bin/bash", "-l", "-c"]

RUN catkin config --cmake-args -DCMAKE_BUILD_TYPE=Release -DGTSAM_TANGENT_PREINTEGRATION=OFF -DCMAKE_CXX_STANDARD=14 
RUN catkin config --extend /opt/ros/$ROS_DISTRO && catkin create pkg -p src/ kimera_docker


RUN catkin config --merge-devel
WORKDIR $ROS_WS/src/kimera_docker
RUN catkin build -s
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> /root/.profile
RUN git clone https://github.com/MIT-SPARK/Kimera-VIO-ROS.git 

#Remove the develop gtsam branch from compiling
RUN sed -i '13,17d' $ROS_WS/src/Kimera-VIO-ROS/install/kimera_vio_ros_https.rosinstall

RUN wstool init # Use unless wstool is already initialized
RUN wstool merge Kimera-VIO-ROS/install/kimera_vio_ros_https.rosinstall
RUN wstool update 
RUN rosdep install --from-paths . --ignore-src -r -y

#Fix the BOOST issue https://github.com/MIT-SPARK/Kimera-VIO-ROS/issues/205
RUN sed -i '17a #include <boost/concept/assert.hpp>' $ROS_WS/src/Kimera-RPGO/include/KimeraRPGO/utils/GeometryUtils.h
RUN sed -i '18a #include <boost/concept_check.hpp>' $ROS_WS/src/Kimera-RPGO/include/KimeraRPGO/utils/GeometryUtils.h

#RUN catkin build -s
CMD ["bash"]


#Install Kimera Semantics

RUN apt-get install protobuf-compiler autoconf
RUN apt-get install ros-$ROS_DISTRO-cmake-modules

WORKDIR $ROS_WS/src
RUN git clone https://github.com/MIT-SPARK/Kimera-Semantics.git
RUN wstool merge --merge-keep -y Kimera-Semantics/install/kimera_semantics_https.rosinstall
RUN wstool update

RUN catkin build
