import pandas as pd

# Load CSV

#df = pd.read_csv('/home/lauragaspar/catkin_kimera/src/datasets/Resultados/tum/acl_jackal_issue_kimera_distributed_poses_1220.csv')
#df = pd.read_csv('/home/lauragaspar/catkin_kimera/src/datasets/Resultados/acl_jackal/distributed/kimera_distributed_poses_4400.csv')
#df = pd.read_csv('/home/lauragaspar/catkin_kimera/src/datasets/ground_truth/1014/acl_jackal_gt_odom.csv')

choose = "pgo"  # vio/pgo

if choose == "vio":
    # df = pd.read_csv('/home/lauragaspar/catkin_modulo/src/Kimera-VIO-ROS/output_logs/Euroc/traj_vio.csv')
    #df = pd.read_csv('/home/lauragaspar/Dataset_bag_tese/Sequencia2_LabISR_baixo/Kimera/RealSenseIR_new_noincpose1_uselcd1/traj_vio.csv')
    df = pd.read_csv('/home/lauragaspar/DATASET_BAG_TESE/Outdoor_Deec/Kimera/alpha10/traj_vio.csv')

    print(df.columns)
    # Convert timestamps from nanoseconds to seconds
    df['#timestamp'] = df['#timestamp'] / 1e9
    df = df.drop(columns=['vx', 'vy', 'vz', 'bgx', 'bgy', 'bgz', 'bax', 'bay', 'baz'])
    # Reorder and select columns for TUM format (adjust as necessary)
    df_tum = df[['#timestamp', 'y', 'x', 'z', 'qx', 'qy', 'qz', 'qw']]
    #  Applies the coordinate transformation (adjust as necessary)
    #df_tum['x'] = -df_tum['x']
    #df_tum['y'] = -df_tum['y']
    #df_tum['z'] = df_tum['z']
    
    df_tum['x'] = -df_tum['x']
    df_tum['y'] = df_tum['y']
    df_tum['z'] = df_tum['z']
    
    
   # df_tum.to_csv('/home/lauragaspar/catkin_modulo/src/Kimera-VIO-ROS/output_logs/Euroc/traj_vio_modificado.csv', index=False)   
   # df_tum.to_csv('/home/lauragaspar/catkin_modulo/src/Kimera-VIO-ROS/output_logs/Euroc/traj_vio.tum', sep=' ', index=False, header=False)

    df_tum.to_csv('/home/lauragaspar/DATASET_BAG_TESE/Outdoor_Deec/Kimera/alpha10/traj_vio_modificado.csv', index=False)
    
    
     # Save as TUM
    df_tum.to_csv('/home/lauragaspar/DATASET_BAG_TESE/Outdoor_Deec/Kimera/alpha10/traj_vio.tum', sep=' ', index=False, header=False)
 

elif choose == "pgo":
    #df = pd.read_csv('/home/lauragaspar/catkin_modulo/src/Kimera-VIO-ROS/output_logs/Euroc/traj_pgo.csv')
    
    df = pd.read_csv('/home/lauragaspar/DATASET_BAG_TESE/Outdoor_Deec/Kimera/alpha10/traj_pgo.csv')
       
       
    print(df.columns)
    df['#timestamp_kf'] = df['#timestamp_kf'] / 1e9
    df_tum = df[['#timestamp_kf', 'y', 'x', 'z', 'qx', 'qy', 'qz', 'qw']]
    df_tum['x'] = -df_tum['x']
    df_tum['y'] = df_tum['y']
    df_tum['z'] = df_tum['z']
 
   # df_tum.to_csv('/home/lauragaspar/catkin_modulo/src/Kimera-VIO-ROS/output_logs/Euroc/traj_pgo_modificado.csv', index=False)
    #df_tum.to_csv('/home/lauragaspar/catkin_modulo/src/Kimera-VIO-ROS/output_logs/Euroc/traj_pgo.tum', sep=' ', index=False, header=False)
    
    df_tum.to_csv('/home/lauragaspar/DATASET_BAG_TESE/Outdoor_Deec/Kimera/alpha10/traj_pgo_modificado.csv', index=False)
    # Save as TUM
    df_tum.to_csv('/home/lauragaspar/DATASET_BAG_TESE/Outdoor_Deec/Kimera/alpha10/traj_pgo.tum', sep=' ', index=False, header=False)



# Sort by 'pose_index'
#df_sorted = df.sort_values(by='pose_index')
# Apply the coordinate transformation (tx, ty, tz) -> (-tx, -tz, -ty) --> kimera-multi
#df_sorted.to_csv('/home/lauragaspar/catkin_kimera/src/datasets/Resultados/tum/kimera_distributed_poses_4400_modified.csv', index=False)
#df_tum.to_csv('/home/lauragaspar/catkin_modulo/src/Kimera-VIO-ROS/output_logs/Euroc/traj_pgo_modificado.csv', index=False)
#df_tum.to_csv('/home/lauragaspar/catkin_kimera/src/datasets/ground_truth/1014/tum/ola_acl_jackal_gt_odom.tum', sep=' ', index=False, header=False)
