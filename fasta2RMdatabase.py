#!/bin/python

import sys

if len(sys.argv) < 3: 
    print "This formats fasta files for use with RepeatMasker, based upon what information is contained in the starting fasta.  The originating fasta will have been generated for a single species using the MIPS pipeline"
    print "Usage: fasta2RMdatabase.py input_file output_file.fasta taxon"
    print " "
    sys.exit()

formatted_fasta_file = open(sys.argv[2], "w")
original_fasta_file = open(sys.argv[1], "r")
taxon = sys.argv[3]
TE = "\tTransposable element\t" + taxon + "\n"
RE = "\tRetrotransposon\t" + taxon + "\n"
LTR = "\tLTR Retrotransposon\t" + taxon + "\n"
GYP = "\tGypsy\t" + taxon + "\n"
COP = "\tCopia\t" + taxon + "\n"
MUT = "\tMutator\t" + taxon + "\n"
CAC = "\tCACTA\t" + taxon + "\n"


for f in original_fasta_file.readlines():
	if f.__contains__(">TXX"):
		formatted_fasta_file.write(f.replace('\n', TE))
	elif f.__contains__(">RXX"):
	    formatted_fasta_file.write(f.replace('\n', RE))
	elif f.__contains__(">RLX"):
	    formatted_fasta_file.write(f.replace('\n', LTR))
	elif f.__contains__(">RLG"):
	    formatted_fasta_file.write(f.replace('\n', GYP))	
	elif f.__contains__(">RLC"):
	    formatted_fasta_file.write(f.replace('\n', COP))	
	elif f.__contains__(">DTM"):
	    formatted_fasta_file.write(f.replace('\n', MUT))	
	elif f.__contains__(">DTC"):
	    formatted_fasta_file.write(f.replace('\n', CAC))		
	else:
	    formatted_fasta_file.write(f)
		
formatted_fasta_file.close()
original_fasta_file.close()

sys.exit()
