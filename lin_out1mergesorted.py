#python lin_dict0409.py -f1 2086ge200bp.txt -f2 merge1fillup > merge1fillupge200bpsorted
#python lin_dict0409.py -f1 7875ge30bp.txt -f2 3utrge30bp10197merge1 > 3utrge30bp10197merge1sorted
import argparse
parser = argparse.ArgumentParser(description="f1中的第一列f11有一定的排列顺序,f2有n列,其中f11是f21的子集,我们的目的是利用f11中的行来提取f21中的行,并让f21中的行按照f11中的顺序输出出来,用法：python lin_dict0409.py -f1 6spe6384.txt -f2 merge1fillup > merge1fillupsorted")
parser.add_argument("-f2","--file2",help="many columns,tabulated,make sure do not contain blank line")
parser.add_argument("-f1","--file1",help="only one column")
args = parser.parse_args()
d={}
with open(args.file2,"r") as fn2:
    for i in fn2:
        i=i.strip().split()
        d[i[0]]=i[:]
with open(args.file1,"r") as fn1:
    for j in fn1:
        j=j.strip().split()
        if j[0] in d.keys():
            print("\t".join(d[j[0]]))
