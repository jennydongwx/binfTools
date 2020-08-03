Problem:
Given a collection of **t** DNA strings **dna**, find a pattern and a collection of **k**-mers (one from each string) that minimizes the
distance between all possible patterns and all possible collections of k-mers.

Solution:
- Greedy Search with pseudocounts

- Randomized search with gibbs sampler

Sample input file:
Please follow *motif_search_sample_input.txt*.
Input file should Contain **k**, **t**, **dna** (seperated by new line).

Usage:
- To run *greedy_motif_search.py*, use the following command:

python greedy_motif_search.py motif_search_sample_input.txt

- To run *randomized_motif_search.py*, use the following command:

python randomized_motif_search.py motif_search_sample_input.txt N

where N is an integer that specifies the repeated number of trials for the randomized algorithm.
