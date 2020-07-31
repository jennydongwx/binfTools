# Motifs is a t x k motif matrix, where we select a k-mer from each length-n string of the total t DNA strings.


def Freq(motifs):
    '''
    Counting the number of occurrences of each nucleotide in each column of the motif matrix;
    the (i, j)-th element of Freq(Motifs) stores the number of times that nucleotide i appears in column j of Motifs.
    :param motifs:
    :return: freq
    '''
    nuc_dict = {'A': 0, 'C':1, 'G':2, 'T':3}
    t = len(motifs[0])
    freq =[[1] * 4 for i in range(t)]
    for motif in motifs:
        for j in range(t):
            letter = motif[j]
            freq[j][nuc_dict[letter]] +=1
    return freq


def Profile(motifs):
    '''
    Computes the profile of the motifs matrix. The (i,j) position is the frequency of the i-th nucleotide in the j-th
    column of the motif matrix.
    :param motifs:
    :return: profile
    '''
    freq = Freq(motifs)
    profile = []
    for col in freq:
        new_col = []
        for elem in col:
            elem = elem / sum(col)
            new_col.append(elem)
        profile.append(new_col)
    return profile

def Score(motifs):
    '''
    Assuming we have a consensus k-mer where the i-th position is selected from the most frequent nucleotide in each motif
    in the motif matrix, score computes the sum of unpopular choices at each position.
    :param motifs:
    :return: score
    '''
    freq = Freq(motifs)
    score = 0
    for col in freq:
        score += sum(col) - max(col)
    return score