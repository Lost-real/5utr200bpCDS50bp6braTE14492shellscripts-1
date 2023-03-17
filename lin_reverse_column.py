#python lin_reverse_column.py -f1 At5utr200bpmerge1sortedreplacefillup > At5utr200bpmerge1sortedreplacefillupreverse
import argparse
parser = argparse.ArgumentParser(description="假如有1行，10列，分别是a 1 2 3 4 5 6 7 8 9, 目的是输出a 9 8 7 6 5 4 3 2 1 ")
parser.add_argument("-f1","--file1",metavar='输入文件1',help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
with open (args.file1,"r") as f1:
    for i in f1:
        i = i.strip().split()
        a=len(i)
#注意i[a:0:-1]
        print(i[0] + "\t" + "\t".join(i[a:0:-1]))
