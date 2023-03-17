#! /usr/bin/env python
#usage: python hash-always.py -l 1.list -f 2.txt > out.txt
import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()

def filter_length01(base):
    list01=[]
    for j in range(len(base)):
        if base[j] !="-":
            list01.append(base[j])
        else:
            continue
    return (int(len(list01)))
def filter_length02(base):
    list01=[]
    for j in range(len(base)):
        list01.append(base[j])
    return (int(len(list01)))
with open(args.file1,"r") as fn1:
    a1=0
    n=0
    for i in fn1:
        i=i.strip()
        n+=1
        if i.startswith(">"):
            print(i)
            # continue
        else:

            if n==2:
                b=str(i)
        # print(filter_length(b))
            # length=len(i)
                for j in range(len(b)):
                    if "".join(i[j:j+3])=="GTA":
                        c=str(i[0:j+3])
                        # a1=filter_length02(c)

                        # print(c)
                        if filter_length01(c)==50:
                            print("".join(i[j+3:]))
                            a1=filter_length02(c)
                            # print(a1)
            else:
                for k in range(len(b)):
                    if "".join(i[k:k+3])=="GTA":
                        c=str(i[0:k+3])
                        a2=filter_length02(c)
                        # print(a2)
                        if filter_length01(c)==50 and a2==a1:
                            print("".join(i[k+3:]))
                        else:
                            continue
                            # print("yes1")
    # print(m)
