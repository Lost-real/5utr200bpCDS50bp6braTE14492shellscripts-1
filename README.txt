#运行步骤
01：提取200bp 5'UTR序列和50bp CDS序列，然后reverse输出。比如：AT1G01020.1.txt
bash realUTR_extract200bp5UTR+50bpCDSdict0928Reverse.sh
02：对提取到的序列进行比对,clustalw2或者mafft比较都可以,这里是用clustalw2进行比对的，比如：AT1G01020.1.fasta
bash realUTR_clustalw2_alignment.sh or bash realUTR_clustalw2_alignment-1.sh
03: 把比对后的每一序列都调整到同一行,比如：AT1G01020.1.fasta1
bash realUTR_manylinestooneline.sh
04: 检查拟南芥基因的中去掉“gap”后，第48-50位ATG的真实位置，因为会存在gap，所以真实位置一定是大于等于48-50，比如是：58-60。比如：AT1G01020.1.fasta1
bash realUTR_check_the_position_of_ATG.sh
05: 开始截取，如果第58-60位是ATG，则截取，否则，只保留基因名字，比如：AT1G01020.1.fasta12
bash realUTR_cut_UTR_after_alignment.sh
06：统计截取后有基因序列的个数，比如，原来有6个基因，只有3个是和拟南芥的ATG对其的，因此，只截取3个，比如：AT1G01020.1.fasta123
bash realUTR_count_the_line_from_the_fasta123.sh
07: 去除空行,比如，总共6个基因，其中有3个在截取之后，只剩下名字，在进行08步求和之前，需要先把空行给去掉,比如：AT1G01020.1.fasta1234
bash realUTR_remove_the_blank_line_of_sequence01.sh
08: 计算保守型。
bash lin_lijipandasforconservation.sh
09：纵向求和,比如：AT1G01020.1.fasta12345
bash lin_lijipandas_sum_of_all_the_cloumns.sh
