#python lin_fillupfromtheright.py -f1 At5utr200bpmerge1sortedreplace > At5utr200bpmerge1sortedreplacefillup
import argparse
parser = argparse.ArgumentParser(description="假如有10行，每行的列数不同，最长的列为100，最短的为10，目的是用-6填充使每一行都为100列最重要的是左对齐，填充右侧的空缺")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
with open (args.file1,"r") as f1:
    for i in f1:
        i = i.strip().split()
        b = 354 - len(i)
        # print(b)
        c = ["-6"] * b
        # print(c)
        print("\t".join(i[:] + c[:]))
