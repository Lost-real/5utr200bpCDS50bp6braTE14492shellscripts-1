#!/bin/bash
for i in $(ls ../5utr200bpCDS50bp6braTE14492-1/*.fasta12345)
	do
		cat ../5utr200bpCDS50bp6braTE14492-1/$i >> ./At5utrfasta12345merge
	done
