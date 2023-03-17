#!/bin/bash
n=1
while [[ "$n" -le 10000 ]]
	do 
		less At17075-1.txt | awk -v a=$n '{ print $a }' > ../5utr200bp17075/"$n"
		let "n=n+1"
	done
