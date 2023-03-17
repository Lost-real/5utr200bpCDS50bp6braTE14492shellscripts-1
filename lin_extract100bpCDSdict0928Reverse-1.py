#! /usr/bin/env python
#usage: python hash-always.py -f1 1.txt -f2 2.txt > out.txt
import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="可以理解为key")
parser.add_argument("-f2","--file2",help="可以理解为字典1")
parser.add_argument("-f3","--file3",help="可以理解为字典2")
args = parser.parse_args()

d = {}
chl_fasta01 = {}
chl_fasta02 = {}
seq01=[]
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
            chl_fasta01[chl_gene] = fsy_sequence
with open (args.file3,"r") as fn3:
    for row in fn3:
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
            chl_fasta02[chl_gene] = fsy_sequence

for i in d.keys():
    if i in chl_fasta01.keys():
        # chl_fasta01[i]=list(chl_fasta01[i][0:3])
        # chl_fasta01[i].reverse()
        # print(str(i)+"\n"+"".join(chl_fasta01[i]))

        # seq01.append(str(i)+":"+"".join(chl_fasta01[i]))
        # for i in d.keys():
        if i in chl_fasta02.keys():
                # chl_fasta02[i]=list(chl_fasta02[i][0:4])
                # chl_fasta02[i].reverse()

            seq01=chl_fasta01[i][0:200]+chl_fasta02[i][0:100]
            print(str(i)+"\n"+"".join(seq01[-1::-1]))
    else:
        continue
