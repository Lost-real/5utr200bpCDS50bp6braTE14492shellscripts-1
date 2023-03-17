import argparse
parser = argparse.ArgumentParser(description="比如：一个矩阵，(1,1)是233，第一行有1+300列,目的，从左侧第二列开始输出，输出233列")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
with open (args.file1,"r") as f1:
    for i in f1:
        i=i.strip().split()
        # print(i[1:a+1])
        print("\t".join(i[:]))




