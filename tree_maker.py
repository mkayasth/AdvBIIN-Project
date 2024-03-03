from Bio import Phylo

# Read the tree coordinates from the file
with open("tree.txt", "r") as file:
    tree_coords = file.read().strip().rstrip()

# Parse the Newick string to create a Phylo tree object
tree = Phylo.read("tree.txt", "newick")

# Render the tree to an image file
Phylo.draw(tree, branch_labels=lambda c: str(c.branch_length))

