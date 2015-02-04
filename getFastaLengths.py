#!/bin/python
# Corrinne Grover, Feb 2015
# Simple script to calculate the length of sequences and report it in descending order

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_protein
from Bio import SeqIO
import sys
import os

if len(sys.argv) < 2:
    print "This calculates and sorts length the length of sequences contained within a fasta file"
    print "Usage: getFastaLengths.py input_file output_file"
    print " "
    sys.exit()

fasta_file = open(sys.argv[1], "r")
lengths_file = open(sys.argv[2], "w")

name = []
length = []
for record in SeqIO.parse(fasta_file, "fasta"):
    name.append(str(record.id))
    length.append(str(len(record.seq)))

length = map(int, length)
namelength = zip(name,length)
namelength.sort(key=lambda tup: tup[1], reverse = True)

for i in namelength:
    print >> lengths_file, i[0] + "\t" + str(i[1])

lengths_file.close()

sys.exit()
