#!/bin/bash
for i in $(ls ../5utr200bpCDS50bp6braTE14492-1/*.fasta1234|cut -d "/" -f3 )
	do
		mv ../5utr200bpCDS50bp6braTE14492-1/$i ../temporary03/
	done
