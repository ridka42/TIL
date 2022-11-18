32^7
10%%3
10%/%3
346434%%3343  
346434%/%3343

a <- (3 >5) 
b <- (3 >= 3)
c <- (3 < 5)
d <- (3 <= 5) 
e <- (3 == 4) 
f <- (3 != 4) 
vec<-c(a,b,c,d,e,f)
print(vec)
101100010111010110 < 11001011000101011
a <- c(2, 3) & c(3, 4)
b <- c(2, 3) && c(3, 4)
c <- c(2, 3) | c(3, 4)
d <- c(2, 3) || c(3, 4)
e <- !3
myList<-list(a,b,c,d,e)
print(myList)
a=c(1,2,3,4,5)
2<a && a<4
min(c(1,2,3,4,5))
max(c(1,2,3,4,5))
sum(c(1,2,3,4,5))
prod(c(1,2,3,4,5))
factorial(4)
factorial(c(1,2,-3,4))
abs(-3)
abs(c(1,2,-3,-4,5))
mean(c(1,2,5,8,10))
median(c(1,2,5,8,10))
range(c(1,2,3,4,5))
range(c(10,2,4,4,77))
var(c(1,2,5,8,10))
sd(c(1,2,5,8,10))
paste('안녕','하세','요')
paste('안녕','하세','요',sep='/')
paste(c(1,2,3),c('번','번','번번'))
rep(1,5)
rep('a',5)
index <- c(1,2,3)
len <- length(index)
paste(index,rep('번',len))

airline <- c('아시아나항공','에어부산','에어프레미아','에어서울','제주항공','진에어','대한항공','티웨이항공')
flight <- c(1575, 481, 124, 354, 1197, 793, 1670, 859)
passenger <- c(249792,90985,29238,71213,203335,133253,250895,146497)
freight <- c(3097.9, 516.7, 111.1, 273.1, 847.1, 763.2, 5406.1, 597.6)
total<- c(sum(flight), sum(passenger), sum(freight))
average <- total/length(airline)
print(total)
print(average)

fligt_index <- flight>mean(flight)
print(fligt_index)
result <- airline[fligt_index]
print(result)

score <- scan()
passScore <- 50
if (score>passScore) {
  print('합격')
} else {
    print('불합격')
}

score<-scan()
if (score >= 90) {
  grade <- 'A'
} else if (score >= 70) {
  grade <- 'B'
} else if (score >= 50) {
  grade <-'C'
} else {
  grade <- 'F'
}
print(paste('당신의 학점은',grade,'입니다'))

score <- c(30,90,75,82)
result <- ifelse(score>=50,print('합격'),print('불합격'))
print(result)

x <-'age'
y<-'name'
result1 <- switch(x,'word'='hi','age'=25,'3'='숫자',NULL)
result2 <- switch(y,'word'='hi','age'=25,'3'='숫자',NULL)
print(result1)
print(result2)

score <- c(30,90,75,82)
result1 <- which(score==90)
print(result1)
result2 <- which(score>=50)
print(result2)

temp<-scan()
if (temp>=30) {
  print('더움')
} else if (20<=temp) {
  print('보통')
} else if ( 10<=temp) {
  print('선선')
} else if (0<=temp) {
  print('추움')
} else {
  print('매우 추움')
}

if (data=='매우 많이'){
  data=100
} else if (data=='많이'){
  data = 70
} else if (data=='보통'){
  data=50
} else if (data=='조금'){
  data=30
} else {
  data = 0
}

switch (data, '매우 많이'=100, '많이'=70, '보통'=50, '조금'=30, 0)

flight <- c(1575, 481, 124, 354, 1197, 793, 1670, 859)
result <- ifelse(flight>=1000, '우수','보통')

airline <- c('아시아나항공','에어부산','에어프레미아','에어서울','제주항공','진에어','대한항공','티웨이항공')
flight <- c(1575, 481, 124, 354, 1197, 793, 1670, 859)
result<-which(flight>mean(flight))
print(airline[result])

for (i in c(1,2,3)){
  print(i)
}
data<-c(32, 45, 21, 10, 43)
result<-0
for (i in data){
  result<-result+i
}
print(result)

data<-c(32, 45, 21, 10, 43)
result<-0
for (i in data){
  result <- ifelse(i>=result, i, result)
}
print(result)

i <- 1
while(i<100){
  i<-2*i
  print(i)
}
i <- 1
while(1){
  i<-2*i

  if(i>100){
    break
  }
  print(i)
}

value<-5
result <-1
i<-1
while (i<=value) {
  result<-i*result
  i<-i+1
}
print(result)

i <- 1
repeat {
  print( i )
  if( i > 9 ) { 
    break
  }
  i <- i + 1 
}
data <- c(32, 45, 21, 10, 43)
data[1]
data[3]
data[1]<-50
data[1]
logic<-c(T,T,F,F,T)
num<-c(1,4,5)
data[logic]
data[num]

data <- c(32, 45, 21, 10, 43)
data[-1]
data[c(-1,-4)]

data <- c(32, 45, 21, 10, 43)
i <-1
while (i<=length(data)) {
  if(data[i]%%2==0){
    print(paste(i,'번째 데이터는 짝수: ',data[i]))
  }
  i<-i+1
}

vec<-c()
i<-1
while (i<=10){
  vec<-c(vec,i)
  i<-i+1
}
print(vec)

data<-c(32, 45, 21, 10, 43)
result<-999999999
for (i in data){
  ifelse(result>i, result<-i, result<-result)
}
print(result)

data<-c(32, 45, 21, 10, 43)
for (i in data){
  if (i %% 2 == 0){
    print(TRUE)
  } else{
    print(FALSE)
  }
}

data<-c(32, 45, 21, 10, 43)
result <- 0
i<-1
while (i <= length(data)){
  if (data[i]%%2==1){
    result<-result+i
  }
  i<-i+1
}
print(result)

airline <- c('아시아나항공','에어부산','에어프레미아','에어서울','제주항공','진에어','대한항공','티웨이항공')
flight <- c(1575, 481, 124, 354, 1197, 793, 1670, 859)

i<-1
vec<-c()
while(i<=length(flight)){
  if (flight[i]>=1000){
    vec<-c(vec,'우수')
  } else {
    vec<-c(vec,'보통')
  }
  i<-i+1
} 
print(vec)

myFunction <- function(){
  print("안녕")
}
myFunction()

mySum <- function(x,y=0){
  result = x+y
  return(result)
}
sum<-mySum(5,10)
sum
mySum(5)

getStatics <- function( x ) { 
  x.mean <- mean(x)
  x.sd <- sd(x)
  x.min <- min(x)
  x.max <- max(x)
  x.summary <- c('mean'=x.mean, 'sd'=x.sd, 'min'=x.min, 'max'=x.max) #index별 이름 설정가능
  return(x.summary)
}
statics <- getStatics(c(1,2,3,4,5))
print(statics)

D_day <- function(year,month,day){
  today<-Sys.Date()
  inputDay<-paste(year,month,day,sep='-')
  inputDay<-as.Date(inputDay)
  Dday <-difftime(today,inputDay)
  return(as.integer(Dday))
}
D_day(2023,01,01)

makeFunction <- function( x ) { 
  power <- function(y) { return(y^x) }
  return(power)
}
square <- makeFunction(2)
cube <- makeFunction(3)
square(5) 
cube(5) 

# student.txt 파일 데이터 가져오기
dir()
data < - read.table('student.txt',header = TRUE, sep=";", encoding = "UTF-8")
data

data<-read.csv('student3.csv',header = FALSE)
dim(data)
print(data)
data<-read.csv('student3.csv',header = FALSE, col.names = c("학번", "이름", "학년", "성적"))

install.packages('readxl')
library(readxl)
data<-read_excel("student4.xlsx")
class(data)
print(data)
exam_data <- read_excel("student4.xlsx",sheet='Exam',na='NULL')
print(exam_data)


homework_data <-read_excel("student4.xlsx",sheet='Homework',range = "R3C1:R8C4")
print(homework_data)

library(datasets)
data <- Orange # ‘Orange’ 데이터셋 사용
print(data)
treeVec <- data$Tree
table(treeVec)

data<-read.csv("TravelMode.csv")
head(data)
dim(data)

yes_index <- which(data$choice=='yes')
yes_data <- data[yes_index, ]
head(yes_data)

pro_data<- yes_data[,c(-1,-2,-4)]
head(pro_data)
str(pro_data)

print(mean(pro_data$wait))
print(mean(pro_data$vcost))
print(mean(pro_data$travel))
print(mean(pro_data$gcost))
print(mean(pro_data$income))

table(pro_data$size)
size_table<-table(pro_data$size)
size_names <- names(size_table)
size_num <- as.numeric(size_table)
one_count<-size_num[which(size_names == '1')]
one_rate <- one_count / sum(size_num)
print(one_rate)
x = 1
y = 2
plot(x,y, ylim=c(0.6,2.0))
x = c(1,2,3,4,5,6)
y = c(2,4,5.8,7,7.5,8)
plot(x,y, pch=19)

x = c(1,2,3,4,5,6)
y = c(2,4,5.8,7,7.5,8)
plot(x,y, type='b', pch=19)

library(datasets)
data <- EuStockMarkets
plot(1:length(data), data, type='l')

plot(1:length(data),data, type="l", main="1991-1998 Europe Stock Daily Closing Price", xlab='day', ylab='price')
x = c(1,2,3,4,5,6)
y = c(2,4,5.8,7,7.5,8)
plot(x, type="o", pch=19, col="red", xlim=c(1,6), ylim=c(1,8))
lines(y, type="o", pch=19, col="green")

data <- as.numeric(AirPassengers)

length(data) #144
y1949 = data[1:12]
y1950 = data[13:24]
plot(y1949, type="o", pch=19, col="red", ylim=c(90,180), xlab="Month", ylab="passengers")
lines(y1950, type="o", pch=19, col="blue")
plot(y1949, type="o", pch=19, col="red", ylim=c(90,180), xlab="Month", ylab="passengers")
lines(y1950, type="o", pch=19, col="blue")
legend("topright", legend=c("1949y", "1950y"), fill=c("red", "blue"))
data <- c(40, 23, 34)
label <- c('A', 'B', 'C')
pie(data, label=label)

research <- c("좋다", '그저 그렇다', '좋다', '좋다', '좋다', '좋다', '싫다', '그저 그렇다', '싫다')
result <- table(research)
pie(result) 
data <- airquality #내장 데이터셋 airquality 사용
head(data)
temp <- data$Temp
range(temp) # 56 97
hist(data$Temp)
hist(data$Temp, breaks=20)
hist(data$Temp, breaks=20, freq=F)

#다중 상자그림
data <- airquality #내장 데이터셋 airquality 사용
head(data)
boxplot(data)

par(mfrow = c(1,1))
data <- airquality
temp <- data$Temp
hist(temp)
hist(temp, breaks=20)


install.packages('readxl')
library(readxl)
data<- read_excel("airport.xlsx", range="R80C3:R85C12" ,col_names=FALSE)
head(data)

airportName <- data$...1
freight <- as.numeric(data$...10)

f_percent <- freight/sum(freight) * 100
f_percent <- round(f_percent, digit = 1)
f_percent
label_data <- paste(airportName,"(",f_percent,"% )")
print(label_data)
pie(f_percent, label=label_data, init.angle=0, radius=1)


data <-read.csv("covid19.csv", header=FALSE,skip = 38, nrows = 30)
head(data)
data <- data[30:1,]
first_vac <- data$V3
first_rate <- data$V5
second_vac <- data$V6
second_rate <- data$V8
second_rate
par(mfrow=c(2,1))
plot(first_vac, type='o', col='red',pch='19',xlab='day',ylab='count', main='코로나 일일 백신 접종수')
lines(second_vac, type = 'o', col='blue',pch='19')
legend('bottomright',legend = c('first','second'),fill=c('red','blue'))
plot(first_rate, type='o', col='red',pch='19',xlab='day',ylab='rate(%)', ylim = c(20,80), main='총 백신 접종률(%)')
lines(second_rate, type = 'o', col='blue',pch='19')
legend('bottomright',legend = c('first','second'),fill=c('red','blue'))

#TraverMode.csv 데이터셋 전처리
data <- read.csv('TravelMode.csv')
head(data)
dim(data) # (840 10)
choice <- data$choice
choice_yes_index <- which(choice == "yes")
choice_yes_index
actual_data <- data[choice_yes_index,] #choice값이 yes인 행과, 그 행들의 모든 열로 이루어진 데이터 프레임
head(actual_data)
processed_data <- actual_data[,c(-1, -2, -4)] # x, individual, choice 칼럼 제거
head(processed_data)
str(processed_data) # 생성한 데이터셋 확인


data_box <- processed_data[,c(2,3,5,6)]
boxplot(data_box)
hist(processed_data$travel)

par(mfrow=c(1,2))
pie(table(processed_data$mode))
pie(table(processed_data$size))
install.packages('dplyr')
library(dplyr)
a<-c(10,22,33)
round(mean(a),digit=1)
a %>% mean %>% round(1)
num<-(round(sqrt(a)+0.2,1)-1)/5
print(paste(num,'%'))

div <- function(x,y){ return(x/y) }
a %>% sqrt() %>% +0.2 %>% round(1) %>% -1 %>% div(5) %>% paste("%") %>% print()
data<-Orange
head(data)
arrange(data, circumference)
arrange(data, circumference, age)%>% tail
arrange(data,age,circumference)%>% tail
distinct(data,age)

id <- as.character(c(2021001:2021010))
math <- c(100, 54, 36, 76, 54, 94, 15, 6, 34,64)
english <- c(95, 23, 11, 89, 50, 53, 70, 13, 60,90)
science <- c(99, 56, 43, 90, 34, 77, 43, 3, 85,72)
exam <- data.frame(id, math, english, science)
print(exam)
select(exam, science, english)
exam[,c('science','english')]
exam %>% filter(science>=70 & math<=50) %>% select(id) %>% as.character() %>% print
print(exam[which(exam$science>=70 & exam$math<=50),c('id')])
mutate(exam,pass=ifelse((math+english+science)/3>=70,'합격','불합격'))
exam[,'pass'] = ifelse((math+english+science)/3>=70,'합격','불합격')
exam
d <- as.character( rep(c(2021001:2021010), tims=2) )
mid_math <- c(100, 54, 36, 76, 54, 94, 15, 6, 34,64)
final_math <- c(90, 80, 23, 67, 44, 72, 10, 45, 87,55)
math <- c(mid_math, final_math)
mid_english <- c(95, 23, 11, 89, 50, 53, 70, 13, 60,90)
final_english <- c(90, 32, 4, 74, 90, 23, 83, 52, 43,70)
english <- c(mid_english, final_english)
mid_science <- c(99, 56, 43, 90, 34, 77, 43, 3, 85,72)
final_science <- c(100, 79, 25, 65, 63, 75, 73, 66, 50, 83)
science <- c(mid_science, final_science)
examTerm <- rep(c('중간', '기말'), times=c(10,10))
exam2 <- data.frame(id, math, english, science, examTerm)
print(exam2)
grouped_exam<-group_by(exam2,id)
summarize(grouped_exam,mathAve = mean(math))
install.packages('gapminder')
library(gapminder)
str(gapminder)
mean(pull(gapminder[gapminder$continent == "Africa", "gdpPercap"]))
mean(pull(gapminder[gapminder$continent == "Americas", "gdpPercap"]))
mean(pull(gapminder[gapminder$continent == "Asia", "gdpPercap"]))
mean(pull(gapminder[gapminder$continent == "Europe", "gdpPercap"]))
mean(pull(gapminder[gapminder$continent == "Oceania", "gdpPercap"]))
mean(pull(gapminder[gapminder$country == 'Korea,Rep.','gdpPercap']))
gapminder %>%  filter(country=='Korea, Rep.') %>% select(gdpPercap) %>% pull() %>% mean()
gdp_conti <- summarize(group_by(gapminder,continent),mean_gdp = mean(gdpPercap))
gdp_conti
America <- gapminder %>% filter(continent=='Americas')
America %>% filter(pop>=30000000)%>% count(country,sort=T)

min <- gapminder %>% filter(country=='Brazil'|country=='Mexico'|country=='United States') %>% select(pop) %>% min()
max <- gapminder %>% filter(country=='Brazil'|country=='Mexico'|country=='United States') %>% select(pop) %>% max()

gapminder %>% filter(country=='Brazil') %>% select(year,pop) %>% plot(type='o',col='red',ylim=c(min,max))
gapminder %>% filter(country=='Mexico') %>% select(year,pop) %>% lines(type='o',col='blue')
gapminder %>% filter(country=='United States') %>% select(year,pop) %>% lines(type='o',col='green')
legend('topleft',legend = c('Brazil','Mexico','United States'), fill=c('red','blue','green'))
library(dplyr)
data <- read.csv('TravelMode.csv')
head(data)
dim(data) # (840 10)
mode_gcost <- data %>% group_by(mode) %>% summarize(gcost_mean = mean(gcost))
mode_gcost<- as.data.frame(mode_gcost)
label<- paste(mode_gcost$mode,"(",round(mode_gcost$gcost_mean/sum(mode_gcost$gcost_mean)*100,1),"%)")
pie(mode_gcost$gcost_mean,labels=label)
