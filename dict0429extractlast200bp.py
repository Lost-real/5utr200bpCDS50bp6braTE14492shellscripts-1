#! /usr/bin/env python
#usage: python hash-always.py -f1 1.txt -f2 2.txt > out.txt
import argparse
parser = argparse.ArgumentParser(description="比如：f2是一个拥有fasta文件的集合，f1是一个文件仅仅有f2中fasta文件的部分名字，注意："
    "此时f2文件中的fasta序列长度各不相同，目的：按照f1中的名单提取序列时仅仅提取，每一个序列的最后200bp")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
parser.add_argument("-f2","--file2",help="the list by which you want to extract from the file")
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
        # print(">"+str(i)+"\n"+chl_fasta[i][300:500])
        print(">" + str(i) + "\n" + chl_fasta[i][len(chl_fasta[i])-200:len(chl_fasta[i])])
    else:
        continue
