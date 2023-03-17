#!/bin/bash

mkfifo tempfifo     #建立命名管道文件
exec 12<>tempfifo   #将管道文件与文件描述符12读写绑定

for i in {1..20}     #设置并发线程的个数，此处为2
do
echo >&12           #对管道输入空行
done

for i in $(ls ../realUTR2774ge200bpnewconservationstructure200bp/*.alifold.out.txt5 | awk -F '/' '{print $3}' | cut -d "." -f1,2)     #任务列表为1-8的数列
do
read -u12           #读取管道中的一行
{
python lin_dict0501.py -f1 ../realUTR2774ge200bpnewconservationstructure200bp/300.txt -f2 ../realUTR2774ge200bpnewconservationstructure200bp/${i}.alifold.out.txt5 > ../realUTR2774ge200bpnewconservationstructure200bp/${i}.alifold.out.txt6
echo >&12           #任务完成后对管道输入空行，补充本次执行任务消耗的空行
}&
done
wait                #等待该循环中所有任务完成

exec 12>&-          #取消写绑定
exec 12<&-          #取消读绑定

rm -rf  tempfifo    #删除命名管道文件
