#!/bin/bash
for i in $( ls ../realUTR2774ge200bpnewconservationstructure/*.aln | cut -d "/" -f3 | cut -d "." -f1,2)
	do 
		RNAalifold --color --aln ../realUTR2774ge200bpnewconservationstructure/${i}.aln && mv ../realUTR2774ge200bpnewconservationstructure/aln.ps ../realUTR2774ge200bpnewconservationstructure/${i}.aln.ps && mv ../realUTR2774ge200bpnewconservationstructure/alirna.ps ../realUTR2774ge200bpnewconservationstructure/${i}.alirna.ps
	done
