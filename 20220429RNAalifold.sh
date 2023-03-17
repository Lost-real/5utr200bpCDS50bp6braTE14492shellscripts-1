#!/bin/bash
for i in $( ls ../realUTR2774ge200bpnewconservationstructure/*.aln | cut -d "/" -f3 | cut -d "." -f1,2)
	do 
		RNAalifold -p $i.aln > $i.out
		mv alifold.out $i.alifold.out.txt
		RNAalifold --color --aln $i.aln
		mv aln.ps $i.aln.ps
		mv alirna.ps $i.alirna.ps
		rm alidot.ps
	done
