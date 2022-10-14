data0<-read.table("/Users/ansonliu/Desktop/CUHK Yr3 Term2/STAT3008/diamond.txt",header=T)
dim(data0)
data1<- data0[seq(641,1641),]
Weight<-data1$Weight; Cut<-data1$Cut; Price<-data1$Price
fit1<-lm(Price~Weight+Cut);summary(fit1)

Call:
lm(formula = Price ~ Weight + Cut)

Residuals:
   Min     1Q Median     3Q    Max 
-935.4 -255.0   10.2  194.4 5008.3 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept) -1598.77      69.61 -22.968   <2e-16 ***
Weight       7864.12      95.42  82.412   <2e-16 ***
Cut           -10.30      23.18  -0.444    0.657    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 434.9 on 998 degrees of freedom
Multiple R-squared:  0.8725,	Adjusted R-squared:  0.8722 
F-statistic:  3414 on 2 and 998 DF,  p-value: < 2.2e-16


RSS<-sum(fit1$residuals^2);RSS
plot(fit1$fitted,rstudent(fit1),xlab="Fitted Value", ylab="Studentized Residuals",cex=1.5)
CutF<-factor(data1$Cut)
fit2<-lm(Price~Weight+CutF:Weight);summary(fit2)

Call:
lm(formula = Price ~ Weight + CutF:Weight)

Residuals:
    Min      1Q  Median      3Q     Max 
-1050.4  -256.0    -1.2   190.6  4975.2 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept)  -1614.94      40.19 -40.181  < 2e-16 ***
Weight        8065.64     150.77  53.496  < 2e-16 ***
Weight:CutF2  -376.99     142.06  -2.654  0.00809 ** 
Weight:CutF3  -181.30     134.28  -1.350  0.17726    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 432.9 on 997 degrees of freedom
Multiple R-squared:  0.8738,	Adjusted R-squared:  0.8734 
F-statistic:  2301 on 3 and 997 DF,  p-value: < 2.2e-16

fit3<-lm(Price~Weight+CutF+CutF:Weight)
anova(fit2,fit3)
summary(fit3)

Call:
lm(formula = Price ~ Weight + CutF + CutF:Weight)

Residuals:
    Min      1Q  Median      3Q     Max 
-1124.8  -261.0    21.6   190.2  4726.2 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept)   -1999.5      135.1 -14.795  < 2e-16 ***
Weight         8830.4      296.0  29.831  < 2e-16 ***
CutF2           748.1      147.9   5.058 5.04e-07 ***
CutF3           140.4      146.1   0.961    0.337    
Weight:CutF2  -1970.7      331.5  -5.945 3.82e-09 ***
Weight:CutF3   -404.2      322.9  -1.252    0.211    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 420 on 995 degrees of freedom
Multiple R-squared:  0.8814,	Adjusted R-squared:  0.8808 
F-statistic:  1479 on 5 and 995 DF,  p-value: < 2.2e-16

RSSfit3<-sum(fit3$residuals^2)
plot(fit3$fitted,rstudent(fit3),xlab="Fitted Value", ylab="Studentized Residuals",cex=1.5)
summary(Price)

Qj-n. Please separately rerun the code

data0<-read.table("/Users/ansonliu/Desktop/CUHK Yr3 Term2/STAT3008/diamond.txt",header=T)
Weight<-data1$Weight; Cut<-data1$Cut; Price<-data1$Price
Price0<-exp(mean(log(Price)))*log(Price);fit0<-lm(Price0~Weight+Cut)
summary(fit0)
sum(fit0$residuals^2)

Call:
lm(formula = Price0 ~ Weight + Cut)

Residuals:
    Min      1Q  Median      3Q     Max 
-406.00  -66.24   -3.53   69.81  304.57 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept) 6263.505     16.472  380.24   <2e-16 ***
Weight      4946.829     22.582  219.06   <2e-16 ***
Cut          139.210      5.486   25.38   <2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 102.9 on 998 degrees of freedom
Multiple R-squared:  0.9804,	Adjusted R-squared:  0.9803 
F-statistic: 2.49e+04 on 2 and 998 DF,  p-value: < 2.2e-16

Price1<-exp(mean(log(Price)))^(1-1)*(Price^1-1)/1;fit1<-lm(Price1~Weight+Cut);sum(fit1$residuals^2)

Price0.5<-exp(mean(log(Price)))^(1-0.5)*(Price^0.5-1)/0.5;fit0.5<-lm(Price0.5~Weight+Cut);sum(fit0.5$residuals^2)

Priceneg0.5<-exp(mean(log(Price)))^(1+0.5)*(Price^(-0.5)-1)/(-0.5);fitneg0.5<-lm(Priceneg0.5~Weight+Cut);sum(fitneg0.5$residuals^2)

Priceneg1<-exp(mean(log(Price)))^(1+1)*(Price^(-1)-1)/(-1);fitneg1<-lm(Priceneg1~Weight+Cut);sum(fitneg1$residuals^2)
