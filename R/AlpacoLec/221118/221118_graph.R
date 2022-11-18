install.packages('dplyr')
install.packages('ggplot2')
library(ggplot2)
diamond = diamonds
str(diamond)
qplot(data=diamonds, x=carat, y=price, aes(col=cut))
qplot(data=diamonds, x=cut, y=price, aes(col=clarity),geom='boxplot')
ggplot(diamonds) # 데이터셋으로 diamonds가 지정됨
ggplot(diamonds, aes(x = carat, y = price)) 
# x축으로 carat, y축으로 price가 지정됨
ggplot(diamonds, aes(x = carat, y = price, color = cut)) 
# cut에 따라 색이 서로 다르게 지정됨
ggplot(diamonds, aes(x = carat, y = price, color = cut)) + geom_point()
ggplot(diamonds, aes(x = carat, y = price)) +
  geom_point()
ggplot(diamonds, aes(x = carat, y = price)) +
  geom_point(shape=21, color='blue', fill='black')
ggplot(diamonds, aes(x = carat, y = price, col=cut)) +
  geom_point(shape=11)
ggplot(diamonds, aes(x=carat, y=price)) +
  geom_point(shape=11, mapping = aes(col=cut))
ggplot(diamonds[1:100,], aes(x=carat,y=price))+
  geom_line(color='blue', size=2)
ggplot(diamonds, aes(x=cut, fill=clarity))+
  geom_bar()
ggplot(diamonds, aes(x=carat, fill=cut)) + 
  geom_histogram(binwidth = 1)
ggplot(diamonds, aes(x=cut,y=carat, fill=clarity)) +
  geom_boxplot()

install.packages('readxl')
library(readxl)
data<-read_excel('day.xlsx',col_names = TRUE, range = cell_cols(4:12))
data<-data[,c(-3,-4,-6,-8)]
print(data)
library(dplyr)
result<- data %>% names() %>% strsplit(split = "[[:punct:]]")
result
new_name<-c()
for (t in result){
  print(t)
  print(paste('first value: ', t[1]))
  new_name<-c(new_name,t[1])
}
print(new_name)
names(data)<-new_name
data$폭염영향예보[is.na(data$폭염영향예보)]<-'보통'
str(data)
data<- na.omit(data)
str(data)
ggplot(data, mapping = aes(x=최고기온,y=최고체감온도,col=자외선지수)) +
  geom_point() +
  facet_wrap(~자외선지수) +
  stat_smooth(level=0.99) +
  coord_cartesian(ylim = c(20,33)) +
  ggtitle('2021년 9월 대한민국 최고기온 대비 최고체감온도')+
  theme_bw()
