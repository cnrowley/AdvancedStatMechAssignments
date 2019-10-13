pdf("o2-water-trajectory.pdf", width=7, height=7)

data1=read.table('prod_1.unwrap.colvars.traj',  header=FALSE)
attach(data1)

plot(V2, V3, lty="solid", type="l", col="black", xlab="X (\uc5)", ylab="Y (\uc5)", yaxt="n", xlim=c(-25, 25), ylim=c(-25, 25))
grid()

data2=read.table('prod_2.unwrap.colvars.traj',  header=FALSE)
attach(data2)

lines(V2, V3, lty="solid", type="l", col="purple")

data3=read.table('prod_3.unwrap.colvars.traj',  header=FALSE)
attach(data3)

lines(V2, V3, lty="solid", type="l", col="blue")

data4=read.table('prod_4.unwrap.colvars.traj',  header=FALSE)
attach(data4)

lines(V2, V3,lty="solid", type="l", col="red")


data5=read.table('prod_5.unwrap.colvars.traj',  header=FALSE)
attach(data5)

lines(V2, V3,lty="solid", type="l", col="green")


axis(side = 2,
     ## Rotate the labels.
     las = 2,
     ## Adjust the label position.
     mgp = c(2, 0.75, 0))

dev.off()

