#!/bin/bash
n=1
while [[ "$n" -le 7075 ]]
	do 
		less At17075-2.txt | awk -v a=$n '{ print $a }' > ../5utr200bp17075-2/"$n"
		let "n=n+1"
	done
