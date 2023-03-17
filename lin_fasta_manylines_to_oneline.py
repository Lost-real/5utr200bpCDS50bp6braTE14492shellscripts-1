"""将多行文件转换为一行
例：
>001
AAGTCCGGTAA
GGCTAGCTAAC
TTCGAACGACA
>002
GGCTAGCATGA
CACATCGACAC
CAGTAGCATCT
转换为：
>001
AAGTCCGGTAAGGCTAGCTAACTTCGAACGACA
>002
GGCTAGCATGACACATCGACACCAGTAGCATCT
"""
#! /usr/bin/env python
#usage: python hash-always.py -l 1.list -f 2.txt > out.txt
import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
seq={}
with open(args.file1,"r") as fn1:
    for line in fn1:
        if line.startswith('>'):    #判断字符串是否以‘>开始’
            name=line.split()[0]    #以空格为分隔符，并取序列为0的项。
            seq[name]=''
        else:
            seq[name]+=line.replace('\n','')
fn1.close()

for i in seq.keys():
    print(i)
    # print("\n")#注意linux上不用"\n",win上需要"\n"
    print(seq[i])
    # print("\n")
#     fw.write(i)
#     fw.write('\n')
#     fw.write(seq[i])
#     fw.write('\n')
# fr.close()