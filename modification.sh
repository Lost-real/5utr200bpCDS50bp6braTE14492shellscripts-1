#!/bin/bash
for i in $(ls ../5utrge30bp9099/*.out1 | cut -d "/" -f3)
	do
		less ../5utrge30bp9099/${i}| sed -e 's/\.\.\/5utrge30bp9099\///g' | sed -e 's/\.txt-1234//g' > ../5utrge30bp9099/ ${i}.2
	done
