import sys
from Bio import SeqIO
import subprocess
import os

def run_prokka(input_file, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Iterate over sequences in the FASTA file
    for record in SeqIO.parse(input_file, "fasta"):
        # Create a temporary FASTA file for the current sequence
        temp_fasta = "temp.fasta"
        with open(temp_fasta, "w") as temp:
            SeqIO.write(record, temp, "fasta")
        
        # Run Prokka on the temporary FASTA file
        strain_name = record.id
        output_prefix = os.path.join(output_dir, strain_name)
        prokka_cmd = ["prokka", temp_fasta, "--outdir", output_prefix, "--kingdom", "Viruses", "--force"]
        subprocess.run(prokka_cmd)
        
        # Remove the temporary FASTA file
        os.remove(temp_fasta)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_dir>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    
    if not os.path.isfile(input_file):
        print("Error: Input file not found.")
        sys.exit(1)
    
    run_prokka(input_file, output_dir)

