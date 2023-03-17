#用于计算多个同源序列的保守性
import pandas as pd
import argparse
parser = argparse.ArgumentParser(description="比如：矩阵有10行100列,第一列是列名,我们想计算整个矩阵的平均值；输出格式：文本名字+整个矩阵的平均值")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()

with open (args.file1,"r") as f1:
    a=pd.read_table(f1,header=None,index_col=0)
    a=a.dropna(axis=1)#按照列索引
    a1=[]
    list=[]
    # print(a)
    a_row_number=a.shape[0]#计算矩阵的行数
    # print(a_row_number)#计算pandas的行数
    # a.loc['Row_mean'] = a.apply(lambda x: x.sum())#计算列的和并把和作为新的一行
    a.loc['Row_mean'] = a.apply(lambda x: x.mean())#计算列的平均值并把平均值作为新的一行
    # print(a)
    list=a.values.tolist()#把矩阵转换成列表
    # print(list[16])
    list1=list[a_row_number]#把列表中的最后一个元素，也就是平均值单独提取出来
def Get_Average(list):
	sum=0
	for i in list:
		sum+=i
	return sum/len(list)
ave=Get_Average(list1)
print (args.file1,ave)
