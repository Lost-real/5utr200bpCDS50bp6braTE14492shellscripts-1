#!/bin/bash
for i in $(ls ../5utr200bpCDS50bp6braTE14492-1/*.fasta1234 | awk -F '/' '{print $3}')
	do
		less ../5utr200bpCDS50bp6braTE14492-1/$i | sed -n '1,1p'|awk '{print $1,NF-1}' >>count002.txt
	done
