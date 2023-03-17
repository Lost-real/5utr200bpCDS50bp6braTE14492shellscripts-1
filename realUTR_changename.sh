#!/bin/bash
for i in $(ls ../5utr200bp17075/* | awk -F '/' '{print $3}')
	do 
		a=$( less ../5utr200bp17075/*$i | sed -n '1,1p')
		mv ../5utr200bp17075/$i ../5utr200bp17075/$a
	done
