import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
n=0
with open(args.file1,"r") as fr:
    for i in fr:
        eachline=i.strip()
        if eachline.startswith(">"):
            n=n+1
        else:
            continue
print(args.file1,n)
