pdf("msd-lm.pdf", width=3.25, height=3.25)

water_data=read.table('o2-water/water.txt',  header=FALSE)
attach(water_data)


water_data.lm2 <- lm(V2 ~ 0 + V1, data=water_data)
summary(water_data.lm2) 

labelY=expression(paste("MSD (\uc5"^"2",")"))

plot(V1/1000, V2, lty="solid", type="l", col="red", xlab="t (ps)", ylab=labelY, xaxs="i", yaxs="i", yaxt="n")

pentane_data=read.table('o2-pentane/pentane.txt',  header=FALSE)
attach(pentane_data)

pentane_data.lm2 <- lm(V2 ~ 0 + V1, data=pentane_data)
summary(pentane_data.lm2)

lines(V1/1000, V2, lty="solid", type="l", col="blue")

# add a legend 
legend("bottomright", legend=c("water", "pentane"), col=c("red", "blue"), lty=1:1, cex=0.8, bty = "n")

axis(side = 2,
     ## Rotate the labels.
     las = 2,
     ## Adjust the label position.
     mgp = c(2, 0.75, 0))



dev.off()

# save the plot to a pdf

#pdf("diffusion-msd.pdf", width=3.25, height=3.25)

