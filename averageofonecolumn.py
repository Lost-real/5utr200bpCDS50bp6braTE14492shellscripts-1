import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()

with open (args.file1,"r") as f1:
    sum = 0
    n = 0
    for i in f1:
        i = i.strip().split()
        sum += float(i[0])
        n += 1
    print(args.file1,"\t",sum/n)
