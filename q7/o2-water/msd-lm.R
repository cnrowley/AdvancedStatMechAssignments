
pdf("msd-lm.pdf", width=3.25, height=4)
mydata=read.table('water.txt',  header=FALSE)
attach(mydata)

#dev.new(width=3.25, height=4, unit="in")

mydata.lm2 <- lm(V2 ~ 0 + V1, data=mydata)
summary(mydata.lm2) 

plot(V1, V2, lty="solid", type="l", col="red", xlab="time (fs)", ylab="MSD (\uc5^2)", yaxt="n")


#axis(side = 2,
#     ## Rotate the labels.
#     las = 2,
#     ## Adjust the label position.
#     mgp = c(2, 0.75, 0))

lm.scatter2 <- ggplot(mydata, aes(x=V1, y=V2)) + 
  geom_point(color='#2980B9', size = 4) + xlim(c(0, 25)) + 
  geom_abline(intercept=0, slope=mydata.lm2$coefficients[1], color='#2C3E50', size=1.1) + 
  labs(title='Regression through the Origin')


dev.off()

pdf(".pdf", width=7, height=7)

