from Bio import Entrez, SeqIO

Entrez.email = "mkayasth@ramapo.edu"

handle = Entrez.esearch(db="nucleotide", term="SARS-CoV-2 genome", retmax=20)
record = Entrez.read(handle)
idlist = record["IdList"]

print("Records Found:", record["Count"])

print("20 IDs for SARS-CoV-2 genome sequences:\n", idlist)

# Dictionary to store {ID:[accession number, length, sample collection date, country, FASTA sequence]}
sequences_dict = {}

for uid in idlist:
        handle = Entrez.efetch(db="nucleotide", id=uid, rettype="gb", retmode="text")
        record = SeqIO.read(handle, "genbank")
    
        
        accession_number = record.id.split(".")[0]  # Extract accession number from the sequence ID
        collection_date = "Unknown"
        country = "Unknown"
        for feature in record.features:
            if "collection_date" in feature.qualifiers:
                collection_date = feature.qualifiers["collection_date"][0]
            if "country" in feature.qualifiers:
                country = feature.qualifiers["country"][0]
        sequences_dict[uid] = [accession_number, len(record.seq), collection_date, country, str(record.seq)]
        
# Printing the dictionary info.
print("Sequences information stored in dictionary:")
for uid, info in sequences_dict.items():
    print(f"ID: {uid}")
    print(f"Accession Number: {info[0]}")
    print(f"Length: {info[1]}")
    print(f"Collection Date: {info[2]}")
    print(f"Country: {info[3]}")
    print(f"Sequence:\n{info[4]}")

