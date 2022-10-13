college216 <- read.csv( file = "/Users/ansonliu/Desktop/Stanford summer session/STATS216/College.csv")
names(college216)
View(college216)
rownames(college216) = college216[,1]
View(college216)
college216 = college216[,-1]
View(college216)
summary(college216)
college216[,1]=factor(college216[,1])
pairs(college216[,1:10])
View(college216)
plot(college216$Private,college216$Outstate)
Elite=rep("No",nrow(college216))
Elite[college216$Top10perc>50]="Yes"
Elite=as.factor(Elite)
college216=data.frame(college216,Elite)
summary(college216$Elite)
plot(college216$Elite,college216$Outstate)
par(mfrow=c(2,2))
hist(college216$Top10perc,breaks=10,xlab="Top10perc");
hist(college216$Top25perc,breaks=8,xlab="Top25perc");
hist(college216$Outstate,breaks=5,xlab="Outstate");
hist(college216$Books,breaks=4,xlab="Books")
par(mfrow=c(2,2))
hist(college216$Personal,breaks=15,xlab="Personal");
hist(college216$PhD,breaks=10,xlab="Phd");
hist(college216$Expend,breaks=5,xlab="Expend");
hist(college216$Terminal,breaks=4,xlab="Terminal")

