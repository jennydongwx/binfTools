#!/usr/bin/env python
# coding: utf-8

import random
import sys
# import helper functions
from motif_search_basics import *


def ProfileRandomKmer(text, profile, k):
    nuc_dict = {'A': 0, 'C':1, 'G':2, 'T':3}
    prob_list = []
    kmers = []
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        prob = 1
        for j in range(k):
            letter = pattern[j]
            prob *= profile[j][nuc_dict[letter]]
        prob_list.append(prob)
        kmers.append(pattern)

    prob_dist = []
    for elem in prob_list:
        elem = elem / sum(prob_list)
        prob_dist.append(elem)
    return random.choices(kmers, weights = prob_dist)[0]


def GibbsSampler(DNA, k, t, N = 2000):
    motifs = []
    best_motifs = []
    # randomly select kmers
    for dna in DNA:
        i = random.randint(0, len(dna) - k)
        motif = dna[i:i+k]
        motifs.append(motif)
        best_motifs.append(motif)

    for j in range(N):
        i = random.randint(0, t-1)
        temp_motifs = motifs[0:i] + motifs[i+1:len(motifs)]
        profile = Profile(temp_motifs)
        motif_i = ProfileRandomKmer(DNA[i], profile, k)
        motifs[i] = motif_i


        if Score(motifs) < Score(best_motifs):
            best_motifs = []
            for motif in motifs:
                best_motifs.append(motif)

    return best_motifs


def main():
    input_filename = sys.argv[1]
    N = int(sys.argv[2])

    k,t,DNA = read_input(input_filename)
    result = GibbsSampler(DNA, k, t, N)
    output = format_output(result, 'r')


if __name__ == "__main__":
    main()
