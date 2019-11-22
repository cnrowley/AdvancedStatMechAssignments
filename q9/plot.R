par(mar = c(1.5, 2, 1, 2))

pdf("folding.pdf", width=3.25, height=7)

foldingData <- read.csv(file = 'folding.dat', header = TRUE)

par(mfrow=c(4,1))
# time,r_gyr,n_hb,sasa,sheet
par(mar = c(4, 4, 3, 1))
plot(foldingData$time, foldingData$r_gyr, type='p', xlab='time (ns)', ylab=expression( paste("r (",  ring(A),  ")")), pch = 20, cex = .6, col = "blue" )

plot(foldingData$time, foldingData$n_hb, type='p', xlab='time (ns)', ylab="number hbonds", pch = 20, cex = .6, col = "blue")
plot(foldingData$time, foldingData$sasa, type='p', xlab='time (ns)', ylab="SASA",  pch = 20, cex = .6, col = "blue") #  ylab=expression( paste("SASA (",  ring(A)^2,  ") "), pch = 16, cex = .6, col = "blue" )
plot(foldingData$time, foldingData$sheet, type='p', xlab='time (ns)', ylab="% beta sheet", pch = 20, cex = .6, col = "blue")
#waterDens[,1], waterDens[,2],xlim = c(-33,33), xlab=expression( paste("z ( ",  ring(A),  ") ") ), ylab=expression(paste("density ( mol / ", ring(A)^3,")")), col="blue", ylim=c(0, 0.012), type="l")

#axis(side = 2,
#     ## Rotate the labels.
#     las = 2,
#     ## Adjust the label position.
#     mgp = c(2, 0.75, 0))

dev.off()

