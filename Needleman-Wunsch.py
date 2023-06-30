#creating the function for the needelman algorithm
def needleman_wunsch(seq1, seq2, match_score=1, mismatch_score=-1, gap_penalty=-1):
    # Create a matrix to store the scores
    n = len(seq1)
    m = len(seq2)
    score_matrix = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize the first row and column
    for i in range(1, n + 1):
        score_matrix[i][0] = score_matrix[i - 1][0] + gap_penalty
    for j in range(1, m + 1):
        score_matrix[0][j] = score_matrix[0][j - 1] + gap_penalty

    # Fill in the score matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                match = match_score
            else:
                match = mismatch_score
            diagonal_score = score_matrix[i - 1][j - 1] + match
            up_score = score_matrix[i - 1][j] + gap_penalty
            left_score = score_matrix[i][j - 1] + gap_penalty
            score_matrix[i][j] = max(diagonal_score, up_score, left_score)

    # Traceback to find the alignment
    align1 = ""
    align2 = ""
    i = n
    j = m
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            match = match_score
        else:
            match = mismatch_score
        if score_matrix[i][j] == score_matrix[i - 1][j - 1] + match:
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1
        elif score_matrix[i][j] == score_matrix[i - 1][j] + gap_penalty:
            align1 = seq1[i - 1] + align1
            align2 = "-" + align2
            i -= 1
        else:
            align1 = "-" + align1
            align2 = seq2[j - 1] + align2
            j -= 1

    while i > 0:
        align1 = seq1[i - 1] + align1
        align2 = "-" + align2
        i -= 1
    while j > 0:
        align1 = "-" + align1
        align2 = seq2[j - 1] + align2
        j -= 1

    return align1, align2

# Example usage
seq1 = "AGTACGCA"
seq2 = "TATGC"
alignment1, alignment2 = needleman_wunsch(seq1, seq2)
print("Alignment 1:", alignment1)
print("Alignment 2:", alignment2)
