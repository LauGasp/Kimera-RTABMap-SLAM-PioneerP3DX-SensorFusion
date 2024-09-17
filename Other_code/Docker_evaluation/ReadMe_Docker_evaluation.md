This project helps you monitor Docker container usage (CPU and Memory) and generate plots in a PDF document.


# Step 1: Record Docker Container Data
To record the resource usage data (CPU and Memory) of your Docker container, first edit the container name in the script.py file, and then run the following script: 

- python run_docker_down_csv.py


This will generate a CSV file with the recorded container data.

# Step 2: Generate a Plot and PDF Report

Once you have the CSV data, you can generate a plot and export it to a PDF file by running:


- python plot_docker_usage.py

This will create a PDF file with CPU and memory usage plotted over time.


