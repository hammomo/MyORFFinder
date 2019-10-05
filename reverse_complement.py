#!/usr/bin/python
# -*- coding: UTF-8 -*-
# reverse_complement.py

class ReverseComplement:
    complement_codon = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    frame_6_set = {
        "Frame +1": "",
        "Frame +2": "",
        "Frame +3": "",
        "Frame -1": "",
        "Frame -2": "",
        "Frame -3": ""
    }

    def __init__(self, sequence):
        self.sequence = sequence.upper()

    def reverse(self, seq):
        return seq[::-1]
    
    def complement(self, seq):
        re = ''
        for char in seq:
            if char == 'N':
                re += char
                continue
            re += self.complement_codon[char]
        return re

    def reverseComplement(self):
        return self.complement(self.reverse(self.sequence))
    
    def fillAll6(self):
        self.frame_6_set['Frame +1'] = self.sequence
        self.frame_6_set['Frame +2'] = self.sequence[1:]
        self.frame_6_set['Frame +3'] = self.sequence[2:]
        rc_version = self.reverseComplement()
        self.frame_6_set['Frame -1'] = rc_version
        self.frame_6_set['Frame -3'] = rc_version[1:]
        self.frame_6_set['Frame -2'] = rc_version[2:]

if __name__ == "__main__":
    f = open('input.fasta', 'r')
    lines = f.readlines()
    seq = ''.join(lines[1:]).replace('\n', '')

    test = ReverseComplement(seq)
    test.fillAll6()
    
    for key in test.frame_6_set:
        print('>', key)
        print(test.frame_6_set[key] + '\n')