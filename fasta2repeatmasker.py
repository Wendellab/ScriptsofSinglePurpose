#!/bin/python

import sys
import os

if len(sys.argv) < 2: 
    print "This formats fasta files for use with RepeatMasker, based upon what information is contained in the starting fasta"
    print "Usage: fasta2repeatmasker.py input_file output_file.fasta"
    print " "
    sys.exit()

formatted_fasta_file = open(sys.argv[2], "w")
temp_file = open('temp', 'w')
original_fasta_file = open(sys.argv[1], "r")
TE = "\tTransposable element\tGossypium spp\n"
RE = "\tRetrotransposon\tGossypium spp\n"
LTR = "\tLTR Retrotransposon\tGossypium spp\n"
GYP = "\tGypsy\tGossypium spp\n"
COP = "\tCopia\tGossypium spp\n"
MUT = "\tMutator\tGossypium spp\n"
CAC = "\tCACTA\tGossypium spp\n"
REP = "\trepetitive\tGossypium spp\n"


for f in original_fasta_file.readlines():
	if f.__contains__("#DNA"):
		temp_file.write(f.replace('\n', TE))
	elif f.__contains__("#LINE"):
	    temp_file.write(f.replace('\n', RE))
	elif f.__contains__("#LTR"):
	    temp_file.write(f.replace('\n', LTR))
	elif f.__contains__("#Retro"):
	    temp_file.write(f.replace('\n', RE))
	elif f.__contains__("#gypsy"):
	    temp_file.write(f.replace('\n', GYP))		
	elif f.__contains__("#copia"):
	    temp_file.write(f.replace('\n', COP))
	elif f.__contains__("#Indecisive"):
	    temp_file.write(f.replace('\n', REP))
	elif f.__contains__("_gypsy"):
	    temp_file.write(f.replace('\n', GYP))
	elif f.__contains__("_copia"):
	    temp_file.write(f.replace('\n', COP))
	elif f.__contains__("#retro"):
	    temp_file.write(f.replace('\n', RE))
	elif f.__contains__(".TE_retrotransposon"):
	    temp_file.write(f.replace('\n', RE))
	elif f.__contains__("_mutator"):
	    temp_file.write(f.replace('\n', MUT))
	elif f.__contains__("_hAT"):
	    temp_file.write(f.replace('\n', TE))
	elif f.__contains__(".TE_LTR-retrotransposon"):
	    temp_file.write(f.replace('\n', LTR))
	elif f.__contains__(".TE_non-LTR-retrotransposon"):
	    temp_file.write(f.replace('\n', RE))
	elif f.__contains__(".TE_transp"):
	    temp_file.write(f.replace('\n', TE))
	elif f.__contains__(".TE_Activ"):
	    temp_file.write(f.replace('\n', TE))
	else:
	    temp_file.write(f)
		
temp_file.close()
temp_file = open('temp', 'r')

for f in temp_file.readlines():
	if f.__contains__(">MX"):
		formatted_fasta_file.write(f.replace('spp', 'hirsutum'))
	elif f.__contains__(">GR"):
	    formatted_fasta_file.write(f.replace('spp', 'raimondii'))
	elif f.__contains__(">gr"):
	    formatted_fasta_file.write(f.replace('spp', 'raimondii'))		
	elif f.__contains__(">Gr"):
	    formatted_fasta_file.write(f.replace('spp', 'raimondii'))
	elif f.__contains__(">GAH"):
	    formatted_fasta_file.write(f.replace('spp', 'arboreum'))
	elif f.__contains__(">GM"):
	    formatted_fasta_file.write(f.replace('spp', 'arboreum'))
	elif f.__contains__(">GKH"):
	    formatted_fasta_file.write(f.replace('Gossypium spp', 'Gossypioides kirkii'))
	elif f.__contains__(">Gk"):
	    formatted_fasta_file.write(f.replace('Gossypium spp', 'Gossypioides kirkii'))
	elif f.__contains__(">1"):
	    formatted_fasta_file.write(f.replace('spp', 'hirsutum'))
	elif f.__contains__(">At."):
	    formatted_fasta_file.write(f.replace('spp', 'hirsutum'))
	elif f.__contains__(">Gorge3_max"):
	    formatted_fasta_file.write(f.replace('spp', 'hirsutum'))
	elif f.__contains__(">Gorge3_A"):
	    formatted_fasta_file.write(f.replace('spp', 'herbaceum'))
	elif f.__contains__(">Gorge3_D"):
	    formatted_fasta_file.write(f.replace('spp', 'raimondii'))
	elif f.__contains__(">Gorge3_K"):
	    formatted_fasta_file.write(f.replace('spp', 'exiguum'))
	elif f.__contains__(">GH"):
	    formatted_fasta_file.write(f.replace('spp', 'herbaceum'))
	elif f.__contains__(">GE"):
	    formatted_fasta_file.write(f.replace('spp', 'exiguum'))
	else:
	    formatted_fasta_file.write(f)

		
formatted_fasta_file.close()
temp_file.close()
os.remove('temp')
original_fasta_file.close()

sys.exit()
