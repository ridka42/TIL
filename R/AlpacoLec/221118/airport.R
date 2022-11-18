airline <-c('아시아나항공','에어부산','에어프레미아','에어서울','제주항공','진에어','대한항공','티웨이항공')
flight <- c(1575, 481, 124, 354, 1197, 793, 1670, 859)
passenger <- c(249792,90985,29238,71213,203335,133253,250895,146497)
freight <- c(3097.9, 516.7, 111.1, 273.1, 847.1, 763.2, 5406.1, 597.6)
airport <- data.frame(airline,flight,passenger,freight)
airport
get_airline <- function(){
  return(airline)
}
get_flight <- function(){
  return(flight)
}
get_passenger <- function(){
  return(passenger)
}
get_freight <- function(){
  return(freight)
}

upperAgvAirline_17 <- function(){ #연산자를 사용한 방법
  upperAvg_flight <- flight > mean(flight) # c(TRUE, FALSE, FALSE, FALSE, TRUE, FALSE, TRUE, FALSE)
  result <- airline[upperAvg_flight]
  return(result)
}
upperAgvAirline_18 <- function(){ #조건문을 사용한 방법
  index <- which(flight > mean(flight)) # c(1, 5, 7)
  result <- airline[index]
  return(result)
}
upperAgvAirline_19 <- function(){ #반복문을 사용한 방법
  result <- c() 
  i <- 1
  while(i <= length(airline) ){ # 데이터 모든 값 한번씩 참조
    if(flight[i] > mean(flight)){ # i 번째 항공사의 운항 실적이 평균보다 좋다면
      result <- c(result, airline[i]) # result 벡터에 i 번째 항공사 명 추가
    }
    i <- i + 1
  }
  return(result)
}