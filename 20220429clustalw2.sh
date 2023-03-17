#!/bin/bash
for i in $(ls ../realUTR2774ge200bpnewconservationstructure200bp/*.txt | cut -d '/' -f3 | cut -d "." -f1,2 )
	do 
		clustalw2 ../realUTR2774ge200bpnewconservationstructure200bp/${i}.txt >> out1
		rm ../realUTR2774ge200bpnewconservationstructure200bp/${i}.dnd
	done
