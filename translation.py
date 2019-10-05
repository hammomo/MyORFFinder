#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Translation:
    DNAcodon = {
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
    line_size = 90

    def __init__(self, sequence):
        self.sequence = sequence
        self.chunks = len(sequence)

    def proteinTranslation(self):
        protein = ''
        seq_list = [self.sequence[i:i+self.chunk_size] for i in range(0, self.chunks, self.chunk_size)]
        for dna in seq_list:
            if len(dna) < 3:
                break
            protein += self.DNAcodon[dna]
        # re_list = [protein[i:i+self.line_size] for i in range(0, len(protein), self.line_size)]
        # return '\n'.join(re_list)
        return protein

if __name__ == '__main__':
    f = open('test.sec', 'r')
    lines = f.readlines()
    seq = ''.join(lines[1:]).replace('\n', '')

    print('> frame 1')
    translator = Translation(seq)
    print(translator.proteinTranslation())

    print('> frame 2')
    translator = Translation(seq[1:])
    print(translator.proteinTranslation())

    print('> frame 3')
    translator = Translation(seq[2:])
    print(translator.proteinTranslation())
