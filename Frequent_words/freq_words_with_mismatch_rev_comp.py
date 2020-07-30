#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ReverseComplement(pattern):
    nuc_dict = {'A':'T', 'C':'G', 'T': 'A', 'G': 'C'}
    rev = []
    for letter in pattern:
        rev_letter = nuc_dict[letter]
        rev.append(rev_letter)
    return ''.join(reversed(rev))

# In[2]:


def SymbolToNumber(symbol):
    nuc_dict = {'A': 0, 'C': '1', 'G':2, 'T':3}
    return int(nuc_dict[symbol])

def PatternToNumber(pattern):
    if pattern == '':
        return 0
    symbol = pattern[-1]
    prefix = pattern[:-1]
    return PatternToNumber(prefix) * 4 + SymbolToNumber(symbol)



# In[74]:


def HammingDistance(A,B):
    count = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            count += 1
    return count

def Suffix(pattern):
    return pattern[1:len(pattern)]

def DNeighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'T', 'C', 'G'}
    neighborhood = set()
    suffix_neighbors = DNeighbors(Suffix(pattern), d)
    for text in suffix_neighbors:
        if HammingDistance(Suffix(pattern), text) < d:
            for x in ['A', 'T', 'C', 'G']:
                neighborhood.add(x+text)
                
        else:
            neighborhood.add(pattern[0]+text)
            
    return neighborhood

# In[4]:


def NumberToSymbol(i):
    nuc_dict = {0:'A', 1: 'C', 2:'G', 3: 'T'}
    return nuc_dict[i]

def NumberToPattern(i,k):
    if k == 1:
        return NumberToSymbol(i)
    prefix_idx = int(i / 4)
    r = int(i % 4)
    symbol = NumberToSymbol(r)
    prefix_pattern = NumberToPattern(prefix_idx, k-1)
    return prefix_pattern + symbol

# In[77]:


def Freq_Array_Mismatch(text, k, d):
    freq_array = []
    for i in range(0, 4**k):
        freq_array.append(0)
    
    for i in range(0, len(text)-k+1):
        pattern = text[i: i+k]
        neighborhood = DNeighbors(pattern,d)
        for approxPattern in neighborhood:
            j = PatternToNumber(approxPattern)
            freq_array[j] += 1
    
    return freq_array

# In[116]:


def Freq_Words_Mismatch_Rev_Comp(text, k, d):
    freq_pattern = set()
    freq_array = Freq_Array_Mismatch(text, k, d)
    rev_freq_array = Freq_Array_Mismatch(ReverseComplement(text), k, d)

    total_array = [freq_array[i] + rev_freq_array[i] for i in range(len(freq_array))]
 
    maxCount = max(total_array)

    for i in range(0, 4**k):
        if total_array[i] == maxCount:
            pattern = NumberToPattern(i,k)
            freq_pattern.add(pattern)

    return freq_pattern

# In[112]:


text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'

# In[113]:


k = 7

# In[114]:


d = 3

# In[117]:


freq_words = Freq_Words_Mismatch_Rev_Comp(text,k,d)
out = ''
for i in range(len(freq_words)):
    out += list(freq_words)[i] + ' '
out

# In[ ]:



