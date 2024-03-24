import os
import sys
from Bio import SeqIO
import subprocess
from collections import defaultdict
import argparse
import shutil

def remove_whitespace_and_run_muscle(input_file, muscle_executable='muscle'):

    # temporary file for cleaning the sequences. Removes spaces and makes the sequence ready for NJ algorithm.
    cleaned_file = f"{input_file}_cleaned"
    with open(input_file, 'r') as f_in, open(cleaned_file, 'w') as f_out:
        for line in f_in:
            if line.startswith(">"):
                f_out.write(line.strip() + '\n')
            else:
                f_out.write(line.replace(" ", "").replace("\n", "") + '\n')

    # overwrites the original file with the aligned version produced by Muscle.
    muscle_cmd = [muscle_executable, '-in', cleaned_file, '-out', input_file]
    subprocess.run(muscle_cmd, check=True)

    # remove the temporary file.
    os.remove(cleaned_file)

def annotate_and_group_genes(input_fasta, output_dir, muscle_executable='muscle'):

    # works in intermediate directory, cleaned after the job.
    intermediate_dir = os.path.join(output_dir, "intermediate_files")
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(intermediate_dir, exist_ok=True)
    
    strains = []
    gene_names = defaultdict(int)
    
    for record in SeqIO.parse(input_fasta, "fasta"):
        strain_name = record.id
        temp_fasta = os.path.join(intermediate_dir, f"{strain_name}.fasta")
        with open(temp_fasta, "w") as temp:
            SeqIO.write(record, temp, "fasta")
        
        prokka_output = os.path.join(intermediate_dir, strain_name)
        prokka_cmd = ["prokka", temp_fasta, "--outdir", prokka_output, "--prefix", strain_name, "--kingdom", "Viruses", "--force"]
        subprocess.run(prokka_cmd)
        
        ffn_file = os.path.join(prokka_output, f"{strain_name}.ffn")
        genes = list(SeqIO.parse(ffn_file, "fasta"))
        strains.append((strain_name, genes))
        
    # for each gene, sequences across different strains are being put together in the same .ffn file. 
    for gene_idx in range(max(len(genes) for _, genes in strains)):
        grouped_genes = []
        for strain_name, strain_genes in strains:
            if gene_idx < len(strain_genes):
                gene = strain_genes[gene_idx]
                description_parts = gene.description.split()
                if 'hypothetical' in description_parts or len(description_parts) < 2:
                    protein_name = "hypothetical_protein"
                else:
                    protein_name = " ".join(description_parts[-2:])
                gene.id = f"{strain_name} | {protein_name}"
                gene.description = ""
                grouped_genes.append(gene)

        # managing fasta header texts and file names.
        if grouped_genes:
            base_gene_name = grouped_genes[0].id.split('|')[-1].strip()
            gene_names[base_gene_name] += 1
            count = gene_names[base_gene_name]
            output_file_name = f"{base_gene_name}{('_' + str(count)) if count > 1 else ''}.ffn"
            output_file = os.path.join(output_dir, output_file_name)
            
            with open(output_file, "w") as outfile:
                SeqIO.write(grouped_genes, outfile, "fasta")
            
            # remove whitespace and run Muscle, overwriting the .ffn file.
            remove_whitespace_and_run_muscle(output_file, muscle_executable=muscle_executable)

    # cleanup: removing intermediate directory.
    shutil.rmtree(intermediate_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Annotate genomes, group genes, and align sequences.")
    parser.add_argument("input_fasta", help="The input FASTA file containing genome sequences.")
    parser.add_argument("output_dir", help="Directory to store the final output files.")
    parser.add_argument("--muscle", help="Path to the Muscle executable", default="muscle")
    
    args = parser.parse_args()
    
    if not os.path.isfile(args.input_fasta):
        sys.exit(f"Error: Input file '{args.input_fasta}' not found.")
    
    annotate_and_group_genes(args.input_fasta, args.output_dir, muscle_executable=args.muscle)
