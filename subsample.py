!/bin/python
# Corrinne Grover, Jan 2016
# subsample sequences from a fasta file
# usage: subsample.py filename #seqs_to_randomly_retain



from Bio import SeqIO
from random import sample
import sys
import os

f = open(sys.argv[1], 'r')
subout = open(sys.argv[1] + ".sub", 'w')
numb = int(sys.argv[2])

seqs = SeqIO.parse(f, "fasta")

samps = ((seq.name, seq.seq) for seq in sample(list(seqs),numb))

for samp in samps:
    print >> subout, (">{}\n{}".format(*samp)) 

f.close()
subout.close()
