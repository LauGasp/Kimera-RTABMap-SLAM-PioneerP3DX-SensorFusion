FROM introlab3it/rtabmap_ros:noetic-latest

ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_WS /workspace/catkin_ws

LABEL author="Mario Cristovao <mario.cristovao@isr.uc.pt>"
LABEL maintainer="Mario Cristovao <mario.cristovao@isr.uc.pt>"
LABEL description="Simple RTABMap Docker environment Environment"

#Install dependencies
RUN apt-get update \
  && apt-get install -y curl git \
  && apt-get update \
  && apt-get install -y \
  ros-${ROS_DISTRO}-robot-localization \
  ros-${ROS_DISTRO}-hector-slam \
  python3-catkin-tools \
  && rm -rf /var/lib/apt/lists/* \
  && mkdir -p /workspace/catkin_ws/src

SHELL ["/bin/bash", "-l", "-c"]
WORKDIR ${ROS_WS}

# Build ros package source
RUN catkin config --extend /opt/ros/$ROS_DISTRO && catkin create pkg -p src/ rtabmap_docker


#Compile packages
RUN catkin build -s

RUN echo "source /workspace/catkin_ws/devel/setup.bash" >> /root/.profile

#ENTRYPOINT [ "catkin", "build", "-s" ]
