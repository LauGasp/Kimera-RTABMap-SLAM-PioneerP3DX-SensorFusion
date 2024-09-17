# GPU Utilization Monitoring and Plot Generation

This script captures GPU and memory utilization over time using nvidia-smi and generates a plot that is saved as a PDF document.

# Step-by-Step Instructions:

- Collect the GPU Usage Data:

Run the nvidia-smi command:
       
nvidia-smi --query-gpu=timestamp,utilization.gpu,utilization.memory --format=csv -l 1 > gpu_usage_seq1_ade20k_130seg.csv

- Run the Plot Script

After collecting the data, run the following Python script to generate the plot and save it as a PDF: python plot_gpu_usage.py






