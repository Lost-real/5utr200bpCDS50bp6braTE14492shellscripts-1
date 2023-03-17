#python lin_fillupfromtheleftwithcolumnnames.py -f1 3utrge30bp10197merge1sorted > 3utrge30bp10197merge1sortedfillup
#注意12行的5218是最长一行的行的长度
import argparse
parser = argparse.ArgumentParser(description="假如有1000行，每行长度都不同，最长的行为5217bp，加上第一列的名字长度总共为5218，我们准备把长度不为5218的用-6来填充，输出分隔符为\t")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
with open (args.file1,"r") as f1:
    c=[]
    d=[]
    for i in f1:
        i=i.strip()
        i=i.split()
	#	d=["-6"]*(5218-len(i))
        d=["-6"]*(6383-len(i))
        # print(10-len(i))
        # d=["*"*j for j in range(10-len(i))]
        # print(i[1:3])
        c=i[0:1]+d[:]+i[int(1):len(i)]
        # print(c)
        print("\t".join(c))
