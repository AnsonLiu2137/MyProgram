load("/Users/ansonliu/Downloads/circles.Rdata")
set.seed(2019)
?kmeans
circles
km.circles<-kmeans(circles,2,nstart=20)
plot(circles,col=(km.circles$cluster),main="K=2")
?hclust
hc.single<-hclust(dist(circles),method="single")
plot(hc.single,main="single linkage")
?cutree
hc.single.aftercut<-cutree(hc.single,2)
plot(circles,col=hc.single.aftercut,main="after cut")
r <- circles$x^2 + circles$y^2
theta <- atan ( circles$y / circles$x )
circles.polar <- data.frame (r , theta )
plot ( circles.polar )
km.circles.new<-kmeans(circles.polar,2,nstart=20)
plot(circles.polar,col=(km.circles.new$cluster),main="K=2, with polar coordinate")
