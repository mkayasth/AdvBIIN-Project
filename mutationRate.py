import csv

def read_csv_data(file_path):
    data = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            data[row[0]] = float(row[1])  # Convert values to float for calculation
    return data

def combine_and_calculate_mutation_rate(branch_length_file, genetic_distance_file, output_file):
    branch_lengths = read_csv_data(branch_length_file)
    genetic_distances = read_csv_data(genetic_distance_file)
    
    with open(output_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Strain", "Branch Length", "Genetic Distance", "Approximate Mutation Rate"])
        
        all_strains = set(branch_lengths.keys()) | set(genetic_distances.keys())
        
        for strain in sorted(all_strains):  # Sorting to maintain a consistent order
            branch_length = branch_lengths.get(strain, None)
            genetic_distance = genetic_distances.get(strain, None)
            
            # Calculate mutation rate if both branch length and genetic distance are available
            if branch_length is not None and genetic_distance is not None and branch_length != 0:
                mutation_rate = genetic_distance / branch_length
            else:
                mutation_rate = "N/A"  # Avoid division by zero or missing data
                
            writer.writerow([strain, branch_length if branch_length is not None else "N/A", 
                             genetic_distance if genetic_distance is not None else "N/A", mutation_rate])

branch_length_file = 'branch_length.csv'
genetic_distance_file = 'genetic_distances.csv'
output_file = 'combined_distances_with_mutation_rate.csv'

combine_and_calculate_mutation_rate(branch_length_file, genetic_distance_file, output_file)

print("Data combined successfully with mutation rate calculated.")
