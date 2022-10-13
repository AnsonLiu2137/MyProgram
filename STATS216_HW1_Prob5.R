load("/Users/ansonliu/Downloads/als.RData")
length(train.y)
length(test.y)
summary(train.y)
hist(train.y,breaks=40,xlab="train.y")
colnames(train.X)[1:20]
pairs(train.X[,21:25])
lm.model <- lm(train.y~.,data=train.X)
coef(summary(lm.model))[1:20,1:4]
summary(lm.model)$r.squared
ybar<-predict(lm.model,test.X)
rmse<-mean((test.y-ybar)^2)
rmse
