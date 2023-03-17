#python lin_replace_the_first_column.py -f1 7875ge30bp-1.txt -f2 3utrge30bp10197merge1sortedfillup > 3utrge30bp10197merge1sortedfillupreplace
#python lin_replace_the_first_column.py -f1 17075conservationsorted-1.txt -f2 At5utr200bpmerge1sorted > At5utr200bpmerge1sortedreplace
import argparse
parser = argparse.ArgumentParser(description="f1有两列,分别是f11和f12,f2有n列,其中f11和f21一样,我们的目的是用f12来替换f21,用法:python lin_replace_the_first_column.py -f1 6384.txt -f2 merge1fillupsorted > merge1fillupsortedreplace")
parser.add_argument("-f1","--file1",help="two columns,tabulated,make sure do not contain blank line")
parser.add_argument("-f2","--file2",help="many columns,tabulated,make sure do not contain blank line")
args = parser.parse_args()
d={}
with open(args.file2,"r") as fn2:
    for i in fn2:
        i=i.strip().split()
        # print(i)
        d[i[0]]=i[1:]
    # print(d)
with open(args.file1,"r") as fn1:
    for j in fn1:
        j=j.strip().split()
        if j[0] in d.keys():
            print(j[1]+"\t"+"\t".join(d[j[0]]))
