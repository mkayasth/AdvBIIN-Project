import csv
from Bio import Phylo

# Function to ask user for the reference strain.
def get_user_input():
    user_input = input("Please enter the reference strain (or part of it): ")
    return user_input.strip()

# Function to find the path between the reference strain and the given strain
def find_path_to_reference(tree, target_strain, reference_strain):
    # Find the common ancestor between target and reference
    common_ancestor = tree.common_ancestor({"name": target_strain}, {"name": reference_strain})
    # Calculate the distance from the target to this common ancestor
    target_distance = tree.distance(target_strain, common_ancestor)
    # Calculate the distance from the reference to this common ancestor
    reference_distance = tree.distance(reference_strain, common_ancestor)
    # Total distance is the sum of both distances
    return target_distance + reference_distance

# Main function
def main():
    # Path to the Newick tree file
    tree_file = "tree.txt"
    
    # Path for the output CSV file
    output_file = "branch_length.csv"
    
    # Read the Newick formatted tree from a file
    tree = Phylo.read(tree_file, "newick")
    
    # Ask user for the reference strain
    reference_substr = get_user_input()
    
    # full name of the reference strain in the tree
    reference_strain = None
    for clade in tree.find_clades():
        if clade.name and reference_substr in clade.name:
            reference_strain = clade.name
            break  # Assuming the first match is the desired reference strain
    
    # Check if reference strain was found
    if not reference_strain:
        print(f"No strain containing '{reference_substr}' found in the tree.")
        return
    
    # Collecting distance information
    distances = []
    
    # Extract the branch lengths from all strains to the reference strain
    for clade in tree.find_clades():
        if clade.name and clade.name != reference_strain:
            distance_to_reference = find_path_to_reference(tree, clade.name, reference_strain)
            distances.append([clade.name, distance_to_reference])
    
    # Writing distance information to a CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Strain", "Distance to " + reference_strain])
        writer.writerows(distances)
    
    print(f"Distances have been written to {output_file}")

# Run the main function
if __name__ == "__main__":
    main()

