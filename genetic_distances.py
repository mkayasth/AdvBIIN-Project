import csv

# Function to ask user for the reference strain
def get_user_input():
    user_input = input("Please enter the reference strain (or part of it): ")
    return user_input.strip()

# Function to read genetic distances from the file
def read_genetic_distances(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')  # Assuming tab-delimited file
        headers = next(reader)  # Assuming the first row contains headers
        matrix = {row[0]: row[1:] for row in reader}  # Create a dict for each row
    return headers, matrix

# Main function
def main():
    # File path for the genetic distances
    distance_file = "genetic_distances.txt"
    
    # Path for the output CSV file
    output_file = "genetic_distances.csv"
    
    # Ask user for the reference strain
    reference_substr = get_user_input()
    
    # Read the genetic distance matrix
    headers, matrix = read_genetic_distances(distance_file)
    
    # full name of the reference strain in the headers
    reference_strain = None
    for header in headers:
        if reference_substr in header:
            reference_strain = header
            break
    
    # Check if reference strain was found
    if not reference_strain:
        print(f"No strain containing '{reference_substr}' found in the distance matrix.")
        return
    
    # Index of the reference strain in each row
    ref_index = headers.index(reference_strain)
    
    # Collect genetic distances to reference strain, excluding reference vs. reference
    distances_to_ref = {}
    for strain, distances in matrix.items():
        if strain != reference_strain:  # Exclude reference vs. reference
            distances_to_ref[strain] = distances[ref_index]
    
    # Writing genetic distance information to a CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Strain", "Genetic Distance to " + reference_strain])
        writer.writerows(distances_to_ref.items())
    
    print(f"Genetic distances have been written to {output_file}")

# Run the main function
if __name__ == "__main__":
    main()

