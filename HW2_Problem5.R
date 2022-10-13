load("/Users/ansonliu/Downloads/als.RData")
library(glmnet)
set.seed(2019)
x=model.matrix(train.y~.-1,data=train.X)
y=train.y
lasso.cv=cv.glmnet(x,y,alpha=1)
plot(lasso.cv)
my.lambda=lasso.cv$lambda.1se
my.lambda
nonzero=predict(lasso.cv,s="lambda.1se",type="nonzero")
nonzero
coef(lasso.cv)

testx=model.matrix(test.y~.-1,data=test.X)
ybar<-predict(lasso.cv,testx)
rmse<-(mean((test.y-ybar)^2))^(1/2)
rmse


set.seed(2019)
ridge.cv=cv.glmnet(x,y,alpha=0)
plot(ridge.cv)
my.lambda.ridge=ridge.cv$lambda.1se
my.lambda.ridge
nonzero.ridge=predict(ridge.cv,s="lambda.1se",type="nonzero")
nonzero.ridge
coef(ridge.cv)
ybar.ridge<-predict(ridge.cv,testx)
rmse.ridge<-(mean((test.y-ybar.ridge)^2))^(1/2)
rmse.ridge
