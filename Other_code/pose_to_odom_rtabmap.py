#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry

# Open the TUM file in append mode
tum_path = '/home/lauragaspar/DATASET_BAG_TESE/ISRsea/Sequence4_ISRsea/localization_mode/file_tum.txt'
tum_file = open(tum_path, 'a')
tum_writer = tum_file

def gps_pose_callback(msg):
    # Access Pose from PoseWithCovarianceStamped
    pose = msg.pose.pose

    # Log received pose
    rospy.loginfo("Received pose: x=%f, y=%f, z=%f", pose.position.x, pose.position.y, pose.position.z)

    # Create a new Odometry message
    odom_msg = Odometry()
    odom_msg.header = msg.header

    # Copy pose information to Odometry message
    odom_msg.pose.pose.position.x = pose.position.x
    odom_msg.pose.pose.position.y = pose.position.y
    odom_msg.pose.pose.position.z = pose.position.z
    odom_msg.pose.pose.orientation.x = pose.orientation.x
    odom_msg.pose.pose.orientation.y = pose.orientation.y
    odom_msg.pose.pose.orientation.z = pose.orientation.z
    odom_msg.pose.pose.orientation.w = pose.orientation.w

    # Publish the Odometry message
    odom_pub.publish(odom_msg)

    # Write pose data to TUM format (timestamp x y z qx qy qz qw)
    tum_writer.write(f"{msg.header.stamp.to_sec()} {pose.position.x} {pose.position.y} {pose.position.z} {pose.orientation.x} {pose.orientation.y} {pose.orientation.z} {pose.orientation.w}\n")

    # Confirm data written
    try:
        rospy.loginfo("Pose data written to TUM: timestamp=%f, x=%f, y=%f, z=%f, orientation_x=%f, orientation_y=%f, orientation_z=%f, orientation_w=%f",
                      msg.header.stamp.to_sec(), pose.position.x, pose.position.y, pose.position.z,
                      pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w)
    except TypeError as e:
        rospy.logerr("Logging error: %s", str(e))

def gps_pose_to_odom_listener():
    rospy.init_node('pose_to_odom_listener', anonymous=True)

    # Subscribe to the gps_pose topic
    rospy.Subscriber('/rtabmap/localization_pose', PoseWithCovarianceStamped, gps_pose_callback)

    # Publish to the odom topic
    global odom_pub
    odom_pub = rospy.Publisher('/odom/localization_mode', Odometry, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    try:
        gps_pose_to_odom_listener()
    except rospy.ROSInterruptException:
        pass
    finally:
        # Close the TUM file when the node is shutting down
        tum_file.close()


