h=function(x,z){
  ifelse(x>z,(x-z)^3,0)
}
hs=function(xs,z){
  sapply(xs,function(x)h(x,z))
}
splinebasis=function(xs,zs){
  spline.matrix=matrix(nrow=length(xs),ncol=length(zs)+3);
  spline.matrix[,1]=xs;
  spline.matrix[,2]=xs^2;
  spline.matrix[,3]=xs^3;
  for(i in 1:length(zs)){
    spline.matrix[,i+3]=hs(xs,zs[i])
  }
  spline.matrix;
}
set.seed(2019)
x = runif(100)
y = sin(10*x)
knots = c(1/4,2/4,3/4)
dataFrame.new=data.frame(y,splinebasis(x,knots))
lm.fit<-lm(y~.,data=dataFrame.new)
test.point=seq(0,1,by=0.01)
test=data.frame(splinebasis(test.point,knots))
lm.pred<-predict(lm.fit,newdata=test)
plot(x,y);curve(sin(10*x),0,1,add=TRUE);lines(test.point,lm.pred,col="blue")

par(mfrow=c(3,3))
for (i in 1:9){
  knots=1:i
  knots=knots/(i+1)
  dataFrame.new=data.frame(y,splinebasis(x,knots))
  lm.fit<-lm(y~.,data=dataFrame.new)
  test.point=seq(0,1,by=0.01)
  test=data.frame(splinebasis(test.point,knots))
  lm.pred<-predict(lm.fit,newdata=test)
  plot(x,y);curve(sin(10*x),0,1,add=TRUE);lines(test.point,lm.pred,col="blue")
}



#test.point=seq(0,1,len=100)
#test=data.frame(splinebasis(test.point,knots))
#lm.pred<-predict(lm.fit,newdata=test)
#plot(x,y)
#?curve
#curve(sin(10*x),0,1,add="TRUE")
#?lines
#lines(test.point,lm.pred,col="green")
