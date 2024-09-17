import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Load the data from the CSV file
df = pd.read_csv('/home/lauragaspar/DATASET_BAG_TESE/LabISR/Sequence1_LabISR/Semantic/gpu_usage_seq1_ade20k_130seg.csv')

# Remove whitespace around column names
df.columns = df.columns.str.strip()

# Convert the timestamp column to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Remove the '%' symbols in the utilization columns and convert to float
df['utilization.gpu [%]'] = df['utilization.gpu [%]'].str.replace('%', '').astype(float)
df['utilization.memory [%]'] = df['utilization.memory [%]'].str.replace('%', '').astype(float)

# Calculate the duration in seconds relative to the first timestamp
df['duration_seconds'] = (df['timestamp'] - df['timestamp'].iloc[0]).dt.total_seconds()

# Check if the columns contain the correct data
print(df[['duration_seconds', 'utilization.gpu [%]', 'utilization.memory [%]']].head())

# Convert the duration and utilization columns to NumPy arrays
duration_seconds = df['duration_seconds'].values
gpu_utilization = df['utilization.gpu [%]'].values
memory_utilization = df['utilization.memory [%]'].values

# Create the plot
with PdfPages('gpu_memory_utilization.pdf') as pdf:
    plt.figure(figsize=(8, 4))
    plt.plot(duration_seconds, gpu_utilization, label='GPU Utilization (%)', color='blue', linestyle='-', linewidth=2)
    plt.plot(duration_seconds, memory_utilization, label='Memory Utilization (%)', color='green', linestyle='-', linewidth=2)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14) 

    # Add labels, legend, and grid
    plt.xlabel('Duration (seconds)', fontsize=16, fontweight='bold')
    plt.ylabel('Utilization (%)', fontsize=16, fontweight='bold')
    #plt.title('GPU and Memory Utilization Over Time', fontsize=16, fontweight='bold')
    plt.legend(fontsize=16)
    plt.grid(True)
    plt.tight_layout()

    # Save the current figure to the PDF
    pdf.savefig()  
    plt.close()

print("Plot saved as PDF successfully!")

