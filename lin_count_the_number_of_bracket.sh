#!/bin/bash
for i in $(ls ../3utrgff3ge30bp10197/*.stout | cut -d "/" -f3)
	do
		python lin_count_the_number_of_bracket.py -f1 ../3utrgff3ge30bp10197/${i}  >> 3utrgff3ge30bp10197.txt
	done
