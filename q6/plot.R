library(ggplot2)

pdf("densprofile.pdf", width=7, height=6)

waterDens <- read.csv('water.txt')
tailDens  <- read.csv('tail.txt')
glycerolDens  <- read.csv('glycerol.txt')
headgroupDens <- read.csv('headgroup.txt')
ionDens <- read.csv('ion.txt')

par(mar = c(6, 6, 6, 6))

plot(waterDens[,1], waterDens[,2],xlim = c(-33,33), xlab=expression( paste("z ( ",  ring(A),  ") ") ), ylab=expression(paste("density ( mol / ", ring(A)^3,")")), col="blue", ylim=c(0, 0.012), type="l")
lines(ionDens[,1], ionDens[,2], col="orange")
lines(headgroupDens[,1], headgroupDens[,2], col="red")
lines(glycerolDens[,1], glycerolDens[,2], col="green")
lines(tailDens[,1], tailDens[,2], col="black")
legend(x="topleft", bty = "n", c('water', 'ions', 'headgroups', 'glycerol', 'tails'), col=c('blue', 'orange', 'red', 'green', 'black'),  pch=c("-", "-", "-", "-"))

#axis(side = 2,
#     ## Rotate the labels.
#     las = 2,
#     ## Adjust the label position.
#     mgp = c(2, 0.75, 0))

dev.off()

