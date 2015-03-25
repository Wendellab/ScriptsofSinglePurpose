#!/bin/python
# Corrinne Grover, Mar 2015
# Simple script to split a multi-fasta into individual fasta sequences

import sys
import os
from Bio import SeqIO

if len(sys.argv) < 1:
    print "This program splits an mfasta into files with one sequence each"
    print "Usage: mfasta2fastas.py fastafile ..."
    print " "
    sys.exit()
	
for record in SeqIO.parse(open(sys.argv[1], 'r'), 'fasta'):
    r = record.id
    filename = "%s.fasta" % r
    handle = open(filename, "w")
    SeqIO.write(record, handle, 'fasta')
    handle.close()

sys.exit()
