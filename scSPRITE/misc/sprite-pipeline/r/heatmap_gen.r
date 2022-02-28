#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)
library(gplots)

max=as.numeric(args[3])

  png(args[2],width = 8, height = 8, units = 'in', res = 300)
	par(oma=c(1, 1, 1, 1))
	a<-read.table(args[1],header=F)
	rownames(a) <- NULL
	colnames(a) <- NULL
	a_matrix <- data.matrix(a)
	a_matrix <- pmin(pmax(data.matrix(a),0),max)
	ramp <- colorRamp(c("white","pink","red","black"))
	a_heatmap <- heatmap.2(cexRow=0.25,cexCol=0.25,a_matrix, Rowv=NA, Colv=NA, col = rgb( ramp(seq(0, 1, length = 200)), max = 255),scale="none",density.info="none",trace="none",dendrogram="none", keysize=1)
	dev.off()

