import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="提取文本中指定的列")
args = parser.parse_args()
with open (args.file1,"r") as f1:
    for i in f1:
        i=i.strip().split()
        i=i[0:1]+i[7413:]
        print("\t".join(i))
