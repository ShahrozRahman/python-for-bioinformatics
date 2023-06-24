from Bio import SeqIO
from Bio import Align
from Bio.Phylo import Phylo
import matplotlib.pyplot as plt

# Step 1: Read sequences from a file
sequences = []
with open('sequences.fasta', 'r') as fasta_file:
    for record in SeqIO.parse(fasta_file, 'fasta'):
        sequences.append(record.seq)

# Step 2: Perform sequence alignment
aligner = Align.PairwiseAligner()
alignments = aligner.align(sequences)

# Step 3: Build a phylogenetic tree
alignment = alignments[0]  # Using the first alignment for simplicity
distances = alignment.substitutions / alignment.length
tree = Phylo.TreeConstruction.DistanceMatrix(names=sequences, matrix=distances)
constructor = Phylo.TreeConstruction.Weighbor(tree)
upgma_tree = constructor.upgma()

# Step 4: Visualize the tree
Phylo.draw(upgma_tree)
plt.show()
