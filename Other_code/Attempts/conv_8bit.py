import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

def process_image(ros_image):
    bridge = CvBridge()
    try:
        # Converte a imagem ROS para uma imagem OpenCV
        cv_image = bridge.imgmsg_to_cv2(ros_image, desired_encoding="passthrough")

        # Verifica as características da imagem original
        rospy.loginfo(f"Original Image dtype: {cv_image.dtype}, min: {cv_image.min()}, max: {cv_image.max()}")

        # Se a imagem não estiver em 8 bits, converta para 8 bits
        if cv_image.dtype != np.uint8:
            # Normaliza a imagem para 8 bits
            cv_image_8bit = cv2.normalize(cv_image, None, 0, 255, cv2.NORM_MINMAX)
            cv_image_8bit = np.uint8(cv_image_8bit)
        else:
            cv_image_8bit = cv_image
        
        # Verifica as características da imagem final
        rospy.loginfo(f"Processed Image dtype: {cv_image_8bit.dtype}, min: {cv_image_8bit.min()}, max: {cv_image_8bit.max()}")

        return cv_image_8bit

    except CvBridgeError as e:
        rospy.logerr("CvBridge Error: {0}".format(e))
        return None

def image_callback_cam0(ros_image):
    cv_image_8bit = process_image(ros_image)
    if cv_image_8bit is not None:
        # Publica a imagem convertida para 8 bits
        image_pub_cam0.publish(cv_bridge.cv2_to_imgmsg(cv_image_8bit, encoding="mono8"))

def image_callback_cam1(ros_image):
    cv_image_8bit = process_image(ros_image)
    if cv_image_8bit is not None:
        # Publica a imagem convertida para 8 bits
        image_pub_cam1.publish(cv_bridge.cv2_to_imgmsg(cv_image_8bit, encoding="mono8"))

def main():
    global cv_bridge, image_pub_cam0, image_pub_cam1
    rospy.init_node('image_converter', anonymous=True)
    
    cv_bridge = CvBridge()

    # Cria publicadores para imagens convertidas
    image_pub_cam0 = rospy.Publisher("/cam0/image_8bit", Image, queue_size=10)
    image_pub_cam1 = rospy.Publisher("/cam1/image_8bit", Image, queue_size=10)

    # Inscreve-se nos tópicos de imagem
    rospy.Subscriber("/cam0/image_raw", Image, image_callback_cam0)
    rospy.Subscriber("/cam1/image_raw", Image, image_callback_cam1)
    
    rospy.spin()

if __name__ == '__main__':
    main()

