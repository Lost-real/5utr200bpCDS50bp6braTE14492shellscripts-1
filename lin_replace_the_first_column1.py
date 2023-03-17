import argparse
parser = argparse.ArgumentParser(description="f1有两列,分别是f11和f12,f2有n列,其中f12和f21一样,我们的目的是用f11来替换f21")
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
        if j[1] in d.keys():
            print(j[0]+"\t"+"\t".join(d[j[1]]))
