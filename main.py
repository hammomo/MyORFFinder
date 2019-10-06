#!/usr/bin/python
# -*- coding: UTF-8 -*-
# main.py & main entrance

import argparse
from reverse_complement import ReverseComplement
from translation import Translation
from find_ORF import FindORF

frame_choices = ['+1', '+2', '+3', '-1', '-2', '-3']
parser = argparse.ArgumentParser(description='An ORF Finder, genome sequence files and output file are in ./test_data folder.')
parser.add_argument('-i', dest='input_files', default='input.fasta', help='input filenames, use \',\' to separate multiple files')
parser.add_argument('-o', dest='output_file', default='output.fasta', help='output filename, only one')
parser.add_argument('-f', dest='frame_number', help='restrict to one single frame', choices=frame_choices)
parser.add_argument('-s', dest='min_size', default=50, type=int, help='define the mininum amino acids for each ORF')
args = parser.parse_args()
read_files = args.input_files.split(',')
write_file = args.output_file
min_size = int(args.min_size)
frame_number = args.frame_number
if frame_number:
    print('Restrict to frame %s' % frame_number)
else:
    print('No valid frame number specified, will find for all 6 frames')

output = open('./test_data/' + write_file, 'w')

def find(input = 'input.fasta', frame = 'all'):
    try:
        f = open('./test_data/' + input, 'r')
        lines = f.readlines()
        name_start = lines[0].split()[0].split('.')[1][:5].upper()
        seq = ''.join(lines[1:]).replace('\n', '')
        all_length = len(seq)
        rc_seqs = ReverseComplement(seq)
        frames_6 = {}
        if (frame_number):
            frames_6 = rc_seqs.fillOneFrame(frame_number)
        else:
            frames_6 = rc_seqs.fillAll6()
        for key in rc_seqs.frame_6_set:
            frames_6[key] = Translation(frames_6[key]).proteinTranslation()
            ORFs = FindORF(frames_6[key], min_size)
            results = ORFs.findLongestORF(key)
            if len(results):
                index = 1
                for start, orf in results.items():
                    if '-' in key:
                        start = all_length - start + 1
                    output.write('>%s_F%s_%04d\t%s\t%d\t%d\n' % (name_start, key[1], index, key, len(orf), start))
                    output.write('\n'.join([orf[i:i+30] for i in range(0,len(orf),30)]) + '\n')
                    index += 1
        print('ORFs have been found for: %s, please check in output file: %s (under ./test_data folder)' % (input, write_file))
    except:
        print('Cannot find file %s under ./test_data folder. Please input exist filename.' % input)

for file in read_files:
    find(input = file)