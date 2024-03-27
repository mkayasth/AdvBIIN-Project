import subprocess
import os
import csv

# paths to Python scripts for mutationRate calculations.
genetic_distances_script = 'genetic_distances.py'
branch_length_script = 'branch_length.py'
mutation_rate_script = 'mutationRate.py'

# path to the final output CSV file from mutationRate.py
mutation_rate_csv = 'combined_distances_with_mutation_rate.csv'

# Function to run a Python script.
def run_script(script_path):
    subprocess.run(['python3.11', script_path], check=True)

# calculate the average mutation rate (for a protein ~ by comparing all with reference strain).
def calculate_average_mutation_rate(csv_file):
    total_mutation_rate = 0
    count = 0
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Approximate Mutation Rate'] != 'N/A':
                total_mutation_rate += float(row['Approximate Mutation Rate'])
                count += 1
    average_mutation_rate = total_mutation_rate / count if count > 0 else 0
    return average_mutation_rate

# Run the scripts in order
run_script(genetic_distances_script)
run_script(branch_length_script)
run_script(mutation_rate_script)

# average mutation rate
average_mutation_rate = calculate_average_mutation_rate(mutation_rate_csv)


# Extracting the protein name from the first strain name in the CSV for naming the variable
with open(mutation_rate_csv, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    first_row = next(reader, None)  # Read the first data row
    if first_row:
        strain_name = first_row[0]
        if '|' in strain_name:
            protein_name = strain_name.split('|')[1].split(',')[0]  # Adjusted to handle additional commas
        else:
            protein_name = 'UnknownProtein'
    else:
        protein_name = 'UnknownProtein'

# Create a variable named dynamically based on the protein name
mutation_rate_dict = {f'mutationRate{protein_name}': average_mutation_rate}

# After processing and calculations are done, delete the files
os.remove('genetic_distances.csv')
os.remove('branch_length.csv')
os.remove('combined_distances_with_mutation_rate.csv')

print(f"Average mutation rate for {protein_name}: {average_mutation_rate}")

