
pdf("alanine.pdf", width=3.25, height=3)
data=read.table('diala.colvars.traj',  header=FALSE)
attach(data)

df = data.frame(V2, V3)
colnames(df) = c("phi","psi")

#dev.new(width=3.25, height=4, unit="in")
plot(df$phi, df$psi,   xlab="phi ", ylab="psi", xlim=c(-180,180), ylim=c(-180,180), pch=20, cex=0.1)

dev.off()

