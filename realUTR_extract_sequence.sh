#!/bin/bash

mkfifo tempfifo     #建立命名管道文件
exec 12<>tempfifo   #将管道文件与文件描述符12读写绑定

for i in {1..10}     #设置并发线程的个数，此处为2
do
echo >&12           #对管道输入空行
done

for i in $(ls ../5utrge30bp14859/AT* | awk -F '/' '{print $3}')     #任务列表为1-8的数列
do
read -u12           #读取管道中的一行
{
python ./lin_extractfulllenghtdict0928.py -f1 ../5utrge30bp14859/$i -f2 ./Brassreal5UTRmerge > ../5utrge30bp14859/$i".txt"
echo >&12           #任务完成后对管道输入空行，补充本次执行任务消耗的空行
}&
done
wait                #等待该循环中所有任务完成

exec 12>&-          #取消写绑定
exec 12<&-          #取消读绑定

rm -rf  tempfifo    #删除命名管道文件
