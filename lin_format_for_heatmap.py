import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
seq={}
# b=open("ztotgen31spAT1G01120.1-1-1-1.txt", 'w')
with open (args.file1,"r") as f1:
    #下面的这个for循环其实就是一个生成字典的过程，需要仔细品味，领悟
    for line in f1:
        if line.startswith('>'):    #判断字符串是否以">"开始
            name=line.strip().split('>')[1]    #以>为分隔符，并取序列为1的项,也就是不带有>的，基因的名字
            # name=line.strip().split()[0]    #以空格为分隔符，并取序列为0的项，也就是带有>的基因的名字
            seq[name]=''
        else:
            seq[name]+=line.replace('\n','')#str.replace(old, new[, max]);old -- 将被替换的子字符串;new -- 新字符串，用于替换old子字符串;max -- 可选字符串, 替换不超过 max 次
    # print(seq)
    # print(seq.keys())
    # a.close()

for i in seq.keys():
    print(i+"\t"+seq[i])
    # b.write(i+"\t"+seq[i]+"\n")#注意windows上面需要用加上"\n",当在linux上运行时，不用加"\n"

# f.close()
