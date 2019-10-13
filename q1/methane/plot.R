pdf("methane-rdf.pdf", width=3.25, height=4)
data=read.table('gofr.dat',  header=FALSE)
attach(data)

#dev.new(width=3.25, height=4, unit="in")

plot(V1, V2, lty="solid", type="l", col="red", xlab="r (\uc5)", ylab="g(r)", yaxt="n", xlim=c(0, 12), ylim=c(0, 3.5))


axis(side = 2,
     ## Rotate the labels.
     las = 2,
     ## Adjust the label position.
     mgp = c(2, 0.75, 0))

dev.off()

