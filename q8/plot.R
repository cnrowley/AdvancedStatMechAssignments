
pdf("rotaxane.pdf", width=3.25, height=4)
#par(mar = c(2, 3, 0, 3)) 
deprot_pmf <- read.csv(file = 'deprotonated/pmf_deprotonated.pmf', col.names = c("z", "pmf"), header=FALSE, comment.char = '#', sep = '')
prot_pmf <- read.csv(file = 'protonated/pmf_protonated.pmf', col.names = c("z", "pmf"), header=TRUE, comment.char = '#', sep = '')

plot(deprot_pmf$z, deprot_pmf$pmf,  lty="solid", type="l", col="red", xlab=expression(paste("z (", ring(A), ")")), ylab="PMF (kcal/mol)",  ylim=c(0, 15))
lines(prot_pmf$z, prot_pmf$pmf, col="blue", type="l")

legend("top", legend=c("deprotonated", "protonated"), col=c('red', 'blue'), bty="n", lwd=c(2,2), cex = 0.8)
dev.off()

