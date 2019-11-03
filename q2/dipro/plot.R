library(ggplot2)

pdf("proline.pdf", width=3.25, height=3)
data=read.table('dipro.colvars.traj',  header=FALSE)
attach(data)

df = data.frame(V2, V3)
colnames(df) = c("phi","psi")

#dev.new(width=3.25, height=4, unit="in")

sp <- ggplot(data=df, aes(phi,psi)) + geom_point(colour="red", size=0.1) 
sp + geom_density_2d()  + theme_linedraw() + labs(x=expression(phi), y=expression(psi)) + scale_y_continuous( limits = c(-180,180), expand = c(0,0) ) + scale_x_continuous( limits = c(-180,180), expand = c(0,0) )

#axis(side = 2,
#     ## Rotate the labels.
#     las = 2,
#     ## Adjust the label position.
#     mgp = c(2, 0.75, 0))

dev.off()

