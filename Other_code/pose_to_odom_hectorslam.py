#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

def gps_pose_callback(msg):
    # Create a new Odometry message
    odom_msg = Odometry()

    # Copy header from gps_pose to odom
    odom_msg.header = msg.header

    # Copy pose information
    odom_msg.pose.pose.position.x = msg.pose.position.x
    odom_msg.pose.pose.position.y = msg.pose.position.y
    odom_msg.pose.pose.position.z = msg.pose.position.z
    odom_msg.pose.pose.orientation.x = msg.pose.orientation.x
    odom_msg.pose.pose.orientation.y = msg.pose.orientation.y
    odom_msg.pose.pose.orientation.z = msg.pose.orientation.z
    odom_msg.pose.pose.orientation.w = msg.pose.orientation.w

    
    
    odom_pub.publish(odom_msg)

def gps_pose_to_odom_listener():
    rospy.init_node('pose_to_odom_listener', anonymous=True)

    # Subscribe to the gps_pose topic
    rospy.Subscriber('/slam_out_pose', PoseStamped, gps_pose_callback)

    # Publish to the odom topic
    global odom_pub
    odom_pub = rospy.Publisher('/odom/lidar2d', Odometry, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    try:
        gps_pose_to_odom_listener()
    except rospy.ROSInterruptException:
        pass

