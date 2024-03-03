def remove_whitespace(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    sequences = []
    current_sequence = ""

    for line in lines:
        if line.startswith(">"):
            # If it's a header line, append the previous sequence (if any) to the list
            if current_sequence:
                sequences.append(current_sequence)
            # Start a new sequence with the header line
            current_sequence = line.strip().rstrip() + '\n'  # Add space after header
        else:
            # Remove whitespace and append to the current sequence
            current_sequence += line.strip().rstrip()

    # Append the last sequence to the list
    if current_sequence:
        sequences.append(current_sequence)

    # Write sequences to the output file
    with open(output_file, 'w') as f:
        for sequence in sequences:
            f.write(sequence + '\n')

# Call the function for your input file
remove_whitespace("aligned_sequences.fna", "new.fna")

