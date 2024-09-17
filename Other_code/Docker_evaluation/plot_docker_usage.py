import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# File name of the CSV
filename = '/home/lauragaspar/Other_code/Docker_evaluation/Seq1_vio_rpgo.csv'

# Load data from the CSV
data = pd.read_csv(filename)

# Remove extra spaces from column names
data.columns = data.columns.str.strip()

# Check the columns present in the CSV file
print("Columns in the CSV file:", data.columns)

# Check the data types of the columns
print(data.dtypes)

# Remove the '%' symbol and convert the 'CPU %' column to float
data['CPU %'] = data['CPU %'].str.rstrip('%').astype(float)

# Convert the 'TIME ELAPSED (s)' column to float
data['TIME ELAPSED (s)'] = data['TIME ELAPSED (s)'].astype(float)

# Function to extract memory usage in GiB
def extract_memory_usage(mem_usage_str):
    try:
        # Extract the memory usage value before the '/' character
        mem_usage = mem_usage_str.split('/')[0].strip()
        # Convert from GiB to float if GiB is in the string
        if 'GiB' in mem_usage:
            return float(mem_usage.replace('GiB', '').strip())
        # Convert from MiB to GiB if MiB is in the string
        elif 'MiB' in mem_usage:
            return float(mem_usage.replace('MiB', '').strip()) / 1024  # Convert MiB to GiB
        else:
            return float(mem_usage)
    except Exception as e:
        print(f"Error parsing memory usage: {e}")
        return None

# Apply the function to create a new column with memory usage in GiB
data['MEMORY USAGE (GiB)'] = data['MEM USAGE / LIMIT'].apply(extract_memory_usage)

# Check the data after the conversion
print(data.head())

# Calculate the average CPU usage
cpu_mean = data['CPU %'].mean()

# Convert columns to NumPy arrays for plotting
x = data['TIME ELAPSED (s)'].values
y_cpu = data['CPU %'].values
y_memory = data['MEMORY USAGE (GiB)'].values

# Create the PDF file using PdfPages
with PdfPages('cpu_memory_usage_plot_with_legend.pdf') as pdf:

    # Plot the data
    fig, ax1 = plt.subplots(figsize=(9,6))

    # Plot the CPU usage
    ax1.plot(x, y_cpu, label='CPU Usage (%)', color='blue', linewidth=2)
    ax1.axhline(y=cpu_mean, color='red', linestyle='--', label=f'Average CPU Usage ({cpu_mean:.2f}%)')
    ax1.set_xlabel('Elapsed Time (s)', fontsize=16, fontweight='bold')
    ax1.set_ylabel('CPU Usage (%)', fontsize=16, fontweight='bold')

    ax1.tick_params(axis='both', which='major', labelsize=16)

    # Add a second y-axis for memory usage
    ax2 = ax1.twinx()
    ax2.plot(x, y_memory, label='Memory Usage (GiB)', color='green', linewidth=2)
    ax2.set_ylabel('Memory Usage (GiB)', fontsize=16, fontweight='bold')
    ax2.tick_params(axis='both', which='major', labelsize=16)

    # Combine the legends of both axes
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc='best', fontsize=16)

    # Add grid
    plt.grid(True)

    # Save the current figure into the PDF file
    pdf.savefig(fig)
    plt.close()  # Close the figure to release memory

print("PDF generated successfully!")


