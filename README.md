# MyORFFinder

Find all possible reading frames (ORF), imitating [ORF finder from NCBI](https://www.ncbi.nlm.nih.gov/orffinder/)

## Description

This project is to find all the possible open reading frames (known as **ORFs**, beginning with **ATG**, and ending with a stop codon, **TGA, TAA, TAG**), accepting standard Fasta format files as input (put them under *./test_data* folder as this repository suggests, default is '*input.fasta*'), and outputing in another Fasta file (default '*output.fasta*').

## Major Steps

The whole project is separated into 3 modules, each tackling one single procedure. (adherent to [Low Coupling, High Cohesion principle](https://medium.com/clarityhub/low-coupling-high-cohesion-3610e35ac4a6))

1. Generate all 6 frames or 1 spcifc frame of original Genome sequence (Nucleotide sequence)

    > reverse_complement.py

2. Translate Nucleotide sequence to Protenin sequence according to [DNA condon table](https://en.wikipedia.org/wiki/DNA_codon_table)

    > translation.py

3. Find the longest ORF from Protein sequence

    > find_ORF.py

## How to Use

The main entrance of this project is > main.py

simply input the following command in command line could apple default values to generate standard output.

* default input file: *input.fasta*
* default output file: *output.fasta*
* default frames: *all 6 frames*
* default minimun size of an ORF: *50*

e.g.:

`python main.py`

It also allows to customise by appending extra arguments, check all valid options by:

`python main.py -h`

And it will provide a **usage** guide.

``` zshell
usage: main.py [-h] [-i INPUT_FILES] [-o OUTPUT_FILES]
               [-f {+1,+2,+3,-1,-2,-3}] [-s MIN_SIZE]

An ORF Finder, genome sequence files and output file are in ./test_data
folder.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILES        input filenames, use ',' to separate multiple files
  -o OUTPUT_FILES       output filename, only one
  -f {+1,+2,+3,-1,-2,-3}
                        restrict to one single frame
  -s MIN_SIZE           define the mininum amino acids for each ORF
```

For example:

`python main.py -i input1.fasta,input2.fasta -o result.fasta -f +1 -s 100`

It will input files *input1.fasta* and *input2.fasta* (2 sequences), only apple frame +1 to read nucleotides, select ORFs which contain not less than 50 amino acids, and finally output result set to *result.fasta*.

## Development Environment

* Darwin MacBook-Pro.local 18.7.0 Darwin Kernel Version 18.7.0: Tue Aug 20 16:57:14 PDT 2019; root:xnu-4903.271.2~2/RELEASE_X86_64 x86_64

* Python 3.7.4

But it is supposed to run properly in any Python3 environment.
