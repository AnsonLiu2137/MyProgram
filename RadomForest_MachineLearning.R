load("/Users/ansonliu/Downloads/body.RData")
train=sample(seq_len(nrow(X)),size=307)
train.X=X[train,]
train.Y=Y[train,]
test.X=X[-train,]
test.Y=Y[-train,]
library(randomForest)
?randomForest
set.seed(2019)
bag.body<-randomForest(train.Y$Weight~.,data=train.X,mtry=21,importance=TRUE,
xtest=test.X,ytest=test.Y$Weight)
rf.body<-randomForest(train.Y$Weight~.,data=train.X,importance=TRUE,xtest=test.X
,ytest=test.Y$Weight)
plot(1:bag.body$ntree,bag.body$test$mse,type="l",xlab="# of trees",
ylab="test MSE",col="red")
lines(1:rf.body$ntree,rf.body$test$mse)
legend("topright",c("Bagging","RadomForest"),lty=c(1,1),col=c("red","black"))
importance(bag.body)
importance(rf.body)
varImpPlot(bag.body)
varImpPlot(rf.body)
