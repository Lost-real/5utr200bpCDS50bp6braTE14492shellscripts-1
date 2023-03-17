import pandas as pd
import argparse
parser = argparse.ArgumentParser(description="矩阵：10行100列，第一列是列名字,想计算每一列的和,输出格式：文本名字+每一列的和")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
with open (args.file1,"r") as f1:
    a=pd.read_table(f1,header=None,index_col=0)
   # a=a.dropna(axis=1)#丢掉含有缺失值的列，axis=1的含义是按照列缺失，axis=0的含义是按照行缺失
    a1=[]
    list=[]
    # print(a)
    a_row_number=a.shape[0]#计算矩阵的行数
    # print(a_row_number)#计算pandas的行数
    a.loc['Row_sum'] = a.apply(lambda x: x.mean())#计算列的和并把和作为新的一行
    # a.loc['Row_mean'] = a.apply(lambda x: x.mean())#计算列的平均值并把平均值作为新的一行
    # print(a)
    list=a.values.tolist()#把矩阵转换成列表
    list1=list[a_row_number]#把列表中的最后一个元素，也就是平均值单独提取出来
    list2=[str(i) for i in list1]#把列表中的元素转化为字符串
    # for i in list2:
        # i=str(i)
        # i=i.split()
    a2="\t".join(list2)#再使用join把字符串拼接起来
    print(args.file1+"\t"+a2)#给输出内容起一个名字和列表的内容，
