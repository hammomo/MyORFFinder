#!/usr/bin/python
# -*- coding: UTF-8 -*-
# find_ORF.py

class FindORF:
    def __init__(self, sequence, min_length):
        self.sequence = sequence
        self.min_length = min_length
    
    def findLongestORF(self):
        ORFs = []
        tmp = ''
        for char in self.sequence:
            if (not tmp) & (char != 'M'):
                continue
            if tmp:
                if char != '*':
                    tmp += char
                else:
                    if (len(tmp) >= self.min_length) & ('X' not in tmp):
                        ORFs.append(tmp)
                    tmp = ''
                continue
            elif char == 'M':
                tmp += char
        if (len(tmp) >= self.min_length) & ('X' not in tmp):
            ORFs.append(tmp)
        return ORFs

if __name__ == "__main__":
    f = open('output.fasta', 'r')
    lines = f.readlines()
    seq = lines[11]
    test = FindORF(seq, 50)
    print(test.findLongestORF())