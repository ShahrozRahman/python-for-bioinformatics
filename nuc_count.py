def calculate_nucleotide_frequency(sequence):
    A_count = 0
    T_count = 0
    C_count = 0
    G_count = 0
    sequence = sequence.upper()
    for nucleotide in sequence:
        if nucleotide == 'A':
            A_count += 1
        elif nucleotide == 'T':
            T_count += 1
        elif nucleotide == 'C':
            C_count += 1
        elif nucleotide == 'G':
            G_count += 1
    print(f'A: {A_count}  T: {T_count}  C: {C_count}  G: {G_count}')
user_sequence = input("Please enter a DNA sequence: ")
calculate_nucleotide_frequency(user_sequence)