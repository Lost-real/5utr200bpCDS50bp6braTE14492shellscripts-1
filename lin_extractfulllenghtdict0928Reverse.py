#! /usr/bin/env python
#usage: python hash-always.py -f1 1.txt -f2 2.txt > out.txt
import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="可以理解为key")
parser.add_argument("-f2","--file2",help="可以理解为字典")
args = parser.parse_args()

d = {}
chl_fasta = {}
with open (args.file1,"r") as fn1:
    for i in fn1:
        i1=i.strip().split()
        d[i1[0]]=1
with open (args.file2,"r") as fn2:
    for row in fn2:
        if ">" in row:
            fsy = row.split()
            chl_gene = fsy[0].replace('>', '')
            fsy_sequence = ''
        else:
            ro=row.strip()
            # print(ro)
            sequences = ro.split()
            # print(row)
            # print(sequences)
            store = sequences[0]
            # print(sequences[0])
            fsy_sequence = fsy_sequence + store
            chl_fasta[chl_gene] = fsy_sequence

for i in d.keys():
    if i in chl_fasta.keys():
        chl_fasta[i]=list(chl_fasta[i])
        chl_fasta[i].reverse()
        print(">"+str(i)+"\n"+"".join(chl_fasta[i]))
    else:
        continue
