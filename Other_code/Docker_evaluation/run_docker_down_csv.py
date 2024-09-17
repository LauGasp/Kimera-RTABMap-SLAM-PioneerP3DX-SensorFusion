import subprocess
import time
import datetime

def get_docker_stats(container_name):
    """
    Retrieves Docker statistics for a specific container.
    """
    try:
        result = subprocess.run(
            ['docker', 'stats', '--no-stream', '--format', '{{.ID}},{{.Name}},{{.CPUPerc}},{{.MemUsage}},{{.MemPerc}},{{.NetIO}},{{.BlockIO}},{{.PIDs}}'],
            capture_output=True,
            text=True,
            check=True
        )
        stats_lines = result.stdout.strip().split('\n')
        # Filter the lines for the specific container
        filtered_stats = [line for line in stats_lines if container_name in line]
        return '\n'.join(filtered_stats)
    except subprocess.CalledProcessError as e:
        print(f"Error executing docker stats: {e}")
        return ""

def is_container_running(container_name):
    """
    Checks if the specified container is running.
    """
    try:
        result = subprocess.run(
            ['docker', 'ps', '--filter', f'name={container_name}', '--format', '{{.Names}}'],
            capture_output=True,
            text=True
        )
        return container_name in result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing docker ps: {e}")
        return False

def is_specific_rosbag_playing(bag_file):
    """
    Checks if 'rosbag play' is running with a specific bag file.
    """
    try:
        result = subprocess.run(
            ['pgrep', '-af', 'rosbag play'],
            capture_output=True,
            text=True
        )
        process_list = result.stdout.strip().split('\n')
        # Check if the specific bag file is found in the process list
        for process in process_list:
            if bag_file in process:
                return True
        return False
    except subprocess.CalledProcessError as e:
        print(f"Error checking rosbag play process: {e}")
        return False

def monitor_container(container_name, bag_file):
    """
    Monitors the specified container and logs its stats while the specific rosbag is being played.
    """
    logging = False
    output_file = f"docker_stats_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    
    # Adds the header to the CSV file
    with open(output_file, 'w') as f:
        f.write("TIME, TIME ELAPSED (s), CONTAINER ID, NAME, CPU %, MEM USAGE / LIMIT, MEM %, NET I/O, BLOCK I/O, PIDS\n")
    
    rosbag_start_time = None
    
    try:
        while True:
            container_running = is_container_running(container_name)
            rosbag_playing = is_specific_rosbag_playing(bag_file)
            
            if container_running:
                if rosbag_playing:
                    if not logging:
                        # Container has just started logging
                        logging = True
                        rosbag_start_time = datetime.datetime.now()
                        print(f"Container '{container_name}' is running and rosbag '{bag_file}' is playing. Logging stats...")
                    
                    # Capture Docker stats
                    stats = get_docker_stats(container_name)
                    
                    if stats:
                        current_time = datetime.datetime.now().strftime('%H:%M:%S')
                        elapsed_time = (datetime.datetime.now() - rosbag_start_time).total_seconds()
                        with open(output_file, 'a') as f:
                            for line in stats.strip().split('\n'):
                                f.write(f"{current_time},{elapsed_time},{line}\n")
                    
                    # Wait for 1 second before the next capture
                    time.sleep(1)
                else:
                    if logging:
                        # Specific rosbag file is not being played, stop logging
                        logging = False
                        print(f"Rosbag file '{bag_file}' is no longer being played. Stopping logging...")
            else:
                if logging:
                    # Container is not running, stop logging
                    logging = False
                    print(f"Container '{container_name}' is no longer running. Stopping logging...")
            
            # Print status messages for debugging
            if not container_running:
                print(f"Container '{container_name}' is not running.")
            if not rosbag_playing:
                print(f"Rosbag file '{bag_file}' is not being played.")
            
            # Wait for 1 second before checking again
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Interrupted by user. Exiting...")

if __name__ == '__main__':
    container_name = "kimera_container"
    bag_file = "ISR_cam15_1_notcut.bag"  # Nome do arquivo rosbag específico
    monitor_container(container_name, bag_file)

