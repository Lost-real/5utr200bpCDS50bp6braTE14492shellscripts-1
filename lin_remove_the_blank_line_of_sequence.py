import argparse
parser = argparse.ArgumentParser(description="矩阵：10行100列，第一列是列名字,想计算每一列的和,输出格式：文本名字+每一列的和")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
with open (args.file1,"r") as f1:
    seq={}
    for i in f1:
        if i.startswith(">"):
            name= i.strip().split('>')[1]
            seq[name]=""
        else:
            seq[name]+=i.replace("\n", "")

    for i in seq.keys():
        if seq[i] !="":
            print(i +"\t"+ seq[i])
    # print(args.file1,n)
