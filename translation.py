#!/usr/bin/python
# -*- coding: UTF-8 -*-
# translation.py
from reverse_complement import ReverseComplement

class Translation:
    DNA_codon = {
        "AAA" : "K", "AAC" : "N", "AAG" : "K", "AAT" : "N",
        "ACA" : "T", "ACC" : "T", "ACG" : "T", "ACT" : "T",
        "AGA" : "R", "AGC" : "S", "AGG" : "R", "AGT" : "S",
        "ATA" : "I", "ATC" : "I", "ATG" : "M", "ATT" : "I",
        "CAA" : "Q", "CAC" : "H", "CAG" : "Q", "CAT" : "H",
        "CCA" : "P", "CCC" : "P", "CCG" : "P", "CCT" : "P",
        "CGA" : "R", "CGC" : "R", "CGG" : "R", "CGT" : "R",	
        "CTA" : "L", "CTC" : "L", "CTG" : "L", "CTT" : "L",
        "GAA" : "E", "GAC" : "D", "GAG" : "E", "GAT" : "D",
        "GCA" : "A", "GCC" : "A", "GCG" : "A", "GCT" : "A",
        "GGA" : "G", "GGC" : "G", "GGG" : "G", "GGT" : "G",
        "GTA" : "V", "GTC" : "V", "GTG" : "V", "GTT" : "V",
        "TAA" : "*", "TAC" : "Y", "TAG" : "*", "TAT" : "Y",
        "TCA" : "S", "TCC" : "S", "TCG" : "S", "TCT" : "S",
        "TGA" : "*", "TGC" : "C", "TGG" : "W", "TGT" : "C",
        "TTA" : "L", "TTC" : "F", "TTG" : "L", "TTT" : "F"  
    }
    chunk_size = 3

    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.chunks = len(sequence)

    def proteinTranslation(self):
        amino_acids = ''
        seq_list = [self.sequence[i:i+self.chunk_size] for i in range(0, self.chunks, self.chunk_size)]
        for dna in seq_list:
            if len(dna) < 3:
                break
            if 'N' in dna:
                amino_acids += 'X'
                continue
            amino_acids += self.DNA_codon[dna]
        return amino_acids

if __name__ == '__main__':
    f = open('input.fasta', 'r')
    lines = f.readlines()
    seq = ''.join(lines[1:]).replace('\n', '')

    test = ReverseComplement(seq)
    test.fillAll6()
    for key in test.frame_6_set:
        print('>', key)
        re = Translation(test.frame_6_set[key]).proteinTranslation()
        print(re)
        
