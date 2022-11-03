# 정규식
# 
# 예시) 주민 등록 번호 901210-2020202 // 뮻-abc 는 잘못된 형태
# 이메일 주소 nadocoding@gmail.com // nadocoding@gmail@gamil.com 은 잘못된 형태 등
# 형태를 체크 할 때 사용

import re

# 교통사고 목격 차가 도망간다 ! 차의 번호판 4자리 문자일경우
# 4글자 중 3개만 기억난다. ca?e 
# care, cafe, cave, cake ,,,, 
# 어떻게 검색할 수 있을까 - ?에 a~z를 넣어본다.

p=re.compile("ca.e") 
# . (ca.e) 은 하나의 문자를 의미 > care, cafe 가능 caffe 불가능
# ^ (^de) 은 문자열의 시작 > desk, destiny 가능 fade 불가능
# $ (se$) 은 문자열의 끝 > case, base 가능 self 불가능

m = p.match("case")
print(m.group()) # 매치 돼서 case 출력됨

m = p.match("caffee")
# print(m.group()) # 매치 안돼서 오류

if m:
  print(m.group())
else:
  print("매칭되지 않음")

# 함수로 만들어 준다.
def print_match(m):
  if m:
    print("m.group():",m.group()) # 일치하는 문자열 반환
    print("m.string:",m.string) 
    # 입력받은 문자열 반환 string은 함수가 아닌 변수기 때문에 ()없이
    print("m.start():",m.start()) # 일치하는 문자열의 시작 index 반환
    print("m.end():",m.end()) # 일치하는 문자열의 끝 index 반환
    print("m.span():",m.span()) # 일치하는 문자열의 시작 과 끝 index 함께 반환
  else:
    print("매칭되지 않음")

m = p.match("careless") 
print_match(m)
# match : 주어진 문자열의 처음부터 일치하는 지 확인한다. 일치함 
m = p.match("good care") 
print_match(m)

m = p.search("good care")
# search : 주어진 문자열 중에 일치하는 게 있는지 -> care 부분이 일치함
print_match(m) # care 출력
m=p.search("careless")
print_match(m) # care 출력

lst = p.findall("careless")
# findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)

lst = p.findall("good care cafe")
print(lst)

# 1. p = re.compile("원하는형태")
# 패턴을 컴파일 해놓는다. 여러번 재사용이 가능
# re.findall("\d{2}","dflds78flksd") 로 바로 사용가능
 
# 2. m=p.match("비교할 문자열")
# 2. lst=p.findall("비교할 문자열") 

# w3school