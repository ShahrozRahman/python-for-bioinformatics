from Bio import Entrez
from Bio import SeqIO

def retrieve_sequences(accession_number):
    # Provide your email address for NCBI's Entrez usage
    Entrez.email = "sheribabu495@gmail.com"

    # Step 1: Search for the protein ID using the accession number
    search_handle = Entrez.esearch(db="protein", term=accession_number)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    if len(search_results["IdList"]) == 0:
        print("No protein ID found for the provided accession number.")
        return

    protein_id = search_results["IdList"][0]

    # Step 2: Retrieve the protein sequence
    protein_handle = Entrez.efetch(db="protein", id=protein_id, rettype="fasta", retmode="text")
    protein_record = SeqIO.read(protein_handle, "fasta")
    protein_sequence = protein_record.seq
    protein_handle.close()

    # Step 3: Search for the mRNA ID using the protein ID
    search_term = "{}[Protein Accession] AND mRNA".format(protein_id)
    search_handle = Entrez.esearch(db="nucleotide", term=search_term)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    if len(search_results["IdList"]) == 0:
        print("No mRNA ID found for the provided protein ID.")
        return

    mrna_id = search_results["IdList"][0]

    # Step 4: Retrieve the mRNA sequence
    mrna_handle = Entrez.efetch(db="nucleotide", id=mrna_id, rettype="fasta", retmode="text")
    mrna_record = SeqIO.read(mrna_handle, "fasta")
    mrna_sequence = mrna_record.seq
    mrna_handle.close()

    # Step 5: Retrieve the nucleotide sequence
    nucleotide_handle = Entrez.efetch(db="nucleotide", id=mrna_id, rettype="fasta_cds_na", retmode="text")
    nucleotide_record = SeqIO.read(nucleotide_handle, "fasta")
    nucleotide_sequence = nucleotide_record.seq
    nucleotide_handle.close()

    # Print the retrieved sequences
    print("Protein Sequence:")
    print(protein_sequence)
    print("\nmRNA Sequence:")
    print(mrna_sequence)
    print("\nNucleotide Sequence:")
    print(nucleotide_sequence)

# Usage: Replace "accession_number_here" with the actual accession number you want to retrieve
retrieve_sequences("NP_200039.1")
