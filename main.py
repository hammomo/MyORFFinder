from reverse_complement import ReverseComplement
from translation import Translation
from find_ORF import FindORF

input = open('./test_data/input.fasta', 'r')
lines = input.readlines()
seq = ''.join(lines[1:]).replace('\n', '')
# seq = ''.join(seq.split())[:50000]
output = open('./test_data/output.fasta', 'w')

test = ReverseComplement(seq)
frames_6 = test.fillAll6()
for key in test.frame_6_set:
    frames_6[key] = Translation(frames_6[key]).proteinTranslation()
    ORFs = FindORF(frames_6[key], 50)
    results = ORFs.findLongestORF()
    if len(results):
        for orf in results:
            output.write('> ' + key + ' ' + str(len(orf)) + '\n')
            output.write(orf + '\n')

output.close()