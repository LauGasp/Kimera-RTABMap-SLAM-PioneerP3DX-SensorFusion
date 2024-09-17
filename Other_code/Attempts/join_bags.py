import rosbag
import rospy
from rospy.rostime import Time

def get_start_time(bag_path):
    """
    Retrieves the start time of a ROS bag.
    """
    with rosbag.Bag(bag_path, 'r') as bag:
        start_time = min(t.to_sec() for _, _, t in bag.read_messages())
    return start_time

def synchronize_and_write_data(bag1_path, bag2_path, output_bag_path):
    """
    Synchronizes timestamps from bag2 to match the start time of bag1 and writes to a new bag.
    """
    start_time_bag1 = get_start_time(bag1_path)
    start_time_bag2 = get_start_time(bag2_path)
    time_offset = start_time_bag1 - start_time_bag2

    with rosbag.Bag(bag1_path, 'r') as bag1, rosbag.Bag(bag2_path, 'r') as bag2, rosbag.Bag(output_bag_path, 'w') as output_bag:
        total_messages_bag1 = sum(1 for _ in bag1.read_messages())
        total_messages_bag2 = sum(1 for _ in bag2.read_messages())
        total_messages = total_messages_bag1 + total_messages_bag2
        messages_written = 0

        # Write data from bag1
        print("Writing data from bag1...")
        for topic, msg, t in bag1.read_messages():
            output_bag.write(topic, msg, t)
            messages_written += 1
            print(f"Writing merged bag: {(messages_written / total_messages) * 100:.2f}% done", end='\r')

        # Write synchronized data from bag2
        print("Writing data from bag2...")
        for topic, msg, t in bag2.read_messages():
            new_time = Time.from_sec(t.to_sec() + time_offset)
            output_bag.write(topic, msg, new_time)
            messages_written += 1
            print(f"Writing merged bag: {(messages_written / total_messages) * 100:.2f}% done", end='\r')
    
    print("\nWriting complete.")

def main():
    bag1_path = '/home/lauragaspar/DATASET_BAG_TESE/Kitchen.bag'
    bag2_path = '/home/lauragaspar/DATASET_BAG_TESE/kitchen_mmseg.bag'
    output_bag_path = '/home/lauragaspar/DATASET_BAG_TESE/kitchen_full.bag'
    
    synchronize_and_write_data(bag1_path, bag2_path, output_bag_path)
    print(f"Merged bag created at {output_bag_path}")

if __name__ == '__main__':
    main()

