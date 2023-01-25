!/usr/bin/env python3

# 22Oct2022 
# By: Mina Peyton
# CSHL Programming for Biolgy - Final Project: Motif Detection
# Input: fasta files 
# Output: motif sequence, start and stop position of motif

from Bio.Seq import Seq
from Bio import SeqUtils

seq = ''
pattern = 'RGKTSANNNNNRGKTSA'
#pattern = Seq(r'[AG]G[GT]T[CG]A.....[AG]G[GT]T[CG]A)')
#print(pattern)

with open('Caenorhabditis_elegans.WBcel235.dna.chromosome.I.fa','r') as raw:
	for line in raw:
		line = line.rstrip()
		if line.startswith('>'):
#			print(line)
			next
		else:
			seq += line

sequence = Seq(seq)
#print(sequence[0:30])
results = SeqUtils.nt_search(str(sequence),pattern)

#print(results)

for i,value in enumerate(results):
	if i == 0:
		continue
	else:
		print(f'Chromosome.1\t',sequence[value:value+len(pattern)],'\t', str(value+1), '\t', str(value + len(pattern)))
