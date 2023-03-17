import argparse
parser = argparse.ArgumentParser(description="文件f1,有只有一列，f11;文件2有2列，f21,f22，其中f21是f11的子集，目的，按照f11的顺序输出f21和f22,如果f11中有f21则输出f21和f22,否则，输出f21和0")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
parser.add_argument("-f2","--file2",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
d={}
with open(args.file2, "r") as f2:
    for i in f2:
        i = i.strip().split()
        d[i[0]] = i[1]


with open (args.file1,"r") as f1:
    for j in f1:
        j = j.strip().split()
        if j[0] in d.keys():
            print(d[j[0]])
        else:
            print("-6")



