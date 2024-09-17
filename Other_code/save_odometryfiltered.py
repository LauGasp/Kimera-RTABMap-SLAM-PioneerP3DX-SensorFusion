import rospy
from nav_msgs.msg import Odometry
import pandas as pd
from datetime import datetime

# Lista para armazenar os dados
data = []

def callback(msg):
    # Extrair dados do tópico
    timestamp = msg.header.stamp.to_sec()  # Convertendo timestamp para segundos
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    z = msg.pose.pose.position.z
    qx = msg.pose.pose.orientation.x
    qy = msg.pose.pose.orientation.y
    qz = msg.pose.pose.orientation.z
    qw = msg.pose.pose.orientation.w
    
    # Adicionar dados à lista
    data.append([timestamp, x, y, z, qx, qy, qz, qw])

def main():
    rospy.init_node('odom_to_csv')
    rospy.Subscriber('/odometry/filtered', Odometry, callback)
    
    # Manter o nó ativo
    rospy.spin()

    # Salvar dados em CSV após a finalização
    df = pd.DataFrame(data, columns=['Timestamp', 'X', 'Y', 'Z', 'QX', 'QY', 'QZ', 'QW'])
    df.to_csv('odometry_data.csv', index=False)

if __name__ == '__main__':
    main()

