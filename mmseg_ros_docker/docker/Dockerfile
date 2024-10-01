ARG PYTORCH="1.10.0"
ARG CUDA="11.3"
ARG CUDNN="8"
ARG MMCV="1.6.0"

FROM pytorch/pytorch:${PYTORCH}-cuda${CUDA}-cudnn${CUDNN}-devel

ENV TORCH_CUDA_ARCH_LIST="6.0 6.1 7.0+PTX"
ENV TORCH_NVCC_FLAGS="-Xfatbin -compress-all"
ENV CMAKE_PREFIX_PATH="$(dirname $(which conda))/../"

# To fix GPG key error when running apt-get update
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub

RUN apt-get update && apt-get install -y git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6 libgl1-mesa-dev lsb-release curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install catkin-tools

RUN conda clean --all

# Install MMCV
ARG PYTORCH
ARG CUDA
ARG MMCV
RUN ["/bin/bash", "-c", "pip install openmim"]
RUN ["/bin/bash", "-c", "mim install mmengine"]
RUN ["/bin/bash", "-c", "mim install mmcv-full==${MMCV}"]


#Install ROS melodic
ENV DEBIAN_FRONTEND=noninteractive

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -
RUN apt update
RUN apt install -y ros-melodic-desktop-full
RUN echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc

WORKDIR /root/catkin_ws/src
WORKDIR /root/catkin_ws

SHELL ["/bin/bash", "-l", "-c"]

# Build ros package source
RUN catkin config --extend /opt/ros/melodic

RUN git clone https://github.com/jianhengLiu/mmsegmentation_ros.git src/mmsegmentation_ros
RUN catkin build -s
RUN source devel/setup.bash

RUN pip install rospkg

# Install MMSegmentation
RUN git clone https://github.com/open-mmlab/mmsegmentation.git /root/catkin_ws/src/mmsegmentation_ros/mmsegmentation
WORKDIR /root/catkin_ws/src/mmsegmentation_ros/mmsegmentation
RUN git checkout 0.x
ENV FORCE_CUDA="1"
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -e .

WORKDIR /root/catkin_ws