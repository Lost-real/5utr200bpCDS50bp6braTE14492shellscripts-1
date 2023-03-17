#rm(list=ls())
library(pheatmap)
library(RColorBrewer)
#library(colorRampPalette)
#getwd()
#创建数据集test测试矩阵
#test = matrix(rnorm(10), 2, 5)

#!/usr/bin/Rscript
# _*_ coding: utf-8 _*_
library(getopt)
 
command=matrix(c( 
     'help', 'h', 0,'loical', '显示此帮助信息',
	 'input', 'i', 2, 'character', '输入文件',
     'output', 'o', 1, 'character', '输出文件'),
			     byrow=T, ncol=5
				 )
args=getopt(command)

# 当未提供参数显示帮助信息
if (!is.null(args$help) || is.null(args$input)) {
	  cat(paste(getopt(command, usage = T), "\n"))
	    q(status=1)
}
 
# 设置默认值
 if ( is.null(args$output)) {
	     args$output = "output.txt"
 }
bmp(file =args$output,width =700*3,height = 750*3,units = "px",res =72*3)
df<- read.table(args$input,header = FALSE,row.names = 1)
#df=apply(df,2,as.numeric)#将df矩阵，逐列转为数值型变量，并再次赋值给test

#test[1:5, seq(1, 5, 2)] = test[1:5, seq(1, 5, 2)]

#rownames(df) = paste("Test", 1:4, sep = "")
#rownames(test) = paste("Gene", 1:2, sep = "")
# 用pheatmap函数画热图
#color=brewer.pal(n =6, name = "RdBu")
#color = colorRampPalette(c("black", "red"))(20)的含义是自定义颜色,show_colnames = F含义是不显示列名
annotation_row = data.frame(
  "Conservation_TE"= factor(rep(c("0.8-0.9: 0.921","0.7-0.8: 0.887","0.6-0.7: 0.888","0.5-0.6: 0.910","0.4-0.5: 0.926","0.3-0.4: 0.921","0.1-0.3: 0.811"), c(111,549,1610,2009,1228,428,86)))
  )#对行进行注释
rownames(annotation_row) = paste("", 1:6021, sep = "")
ann_colors = list(
"Conservation_TE" = c("0.8-0.9: 0.921"="#00FF4DFF","0.7-0.8: 0.887"="#FF00AAFF","0.6-0.7: 0.888"="#FFFF00FF","0.5-0.6: 0.910"="#0000FFFF","0.4-0.5: 0.926"="#FF0000FF","0.3-0.4: 0.921"="#FFAA00FF","0.1-0.3: 0.811"="#AAFF00FF")
	  )#自己调整颜色
pheatmap(df,annotation_row = annotation_row,annotation_colors = ann_colors,cluster_cols = FALSE,cluster_rows = FALSE,color = colorRampPalette(c("white","black","red"))(1800),cellwidth =0.08,cellheight=0.08,show_rownames=F,show_colnames = F,legend_breaks=c(-6:6),border=FALSE,legend_labels = c("-6.0","-5.0","-4.0","-3.0","-2.0","-1.0","0","1.0","2.0","3.0","4.0","5.0","6.0"))
#下面显示的是颜色
#x <- colorRampPalette(c("royalblue","firebrick3"))(12)
#scales::show_col(x)
#write.table(args$output,file=./,quote = FALSE,row.names = FALSE,col.names = FALSE,sep="\t")
