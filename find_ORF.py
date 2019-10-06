#!/usr/bin/python
# -*- coding: UTF-8 -*-
# find_ORF.py
from translation import Translation

class FindORF:
    def __init__(self, sequence, min_length):
        self.sequence = sequence
        self.min_length = min_length
    
    def findLongestORF(self, frame = '+1'):
        ORFs = {}
        tmp = ''
        idx = 0
        if '2' in frame:
            idx = 1
        elif '3' in frame:
            idx = 2
        for char in self.sequence:
            if tmp:
                if char != '*':
                    tmp += char
                else:
                    if (len(tmp) >= self.min_length) & ('X' not in tmp):
                        ORFs[idx - len(tmp)* 3 + 1] = tmp
                    tmp = ''
            elif char == 'M':
                tmp += char
            idx += 3
        if (len(tmp) >= self.min_length) & ('X' not in tmp):
            ORFs[idx - len(tmp)* 3 + 1] = tmp
        return ORFs

if __name__ == "__main__":
    f = open('./test_data/input.fasta', 'r')
    lines = f.readlines()
    seq = ''.join(lines[1:]).replace('\n', '')
    trans = Translation(seq).proteinTranslation()
    print(FindORF(trans,50).findLongestORF())