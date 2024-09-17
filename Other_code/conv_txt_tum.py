def process_file(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as infile:
            # Read all lines from the file
            lines = infile.readlines()

        # Open the output file for writing
        with open(output_file, 'w') as outfile:
            # Iterate over the lines, starting from the second (index 1) to remove the header
            for line in lines[1:]:
                # Replace commas with periods
                converted_line = line.replace(',', '.')
                # Write the converted line to the output file
                outfile.write(converted_line)

        print(f"Processing completed. Check the file '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"Error: {e}")

# Call the function with the desired input and output files
input_file = '/home/lauragaspar/DATASET_BAG_TESE/Outdoor_Deec/GT/GT.txt'
output_file = '/home/lauragaspar/DATASET_BAG_TESE/Outdoor_Deec/GT/GT.tum'
process_file(input_file, output_file)

