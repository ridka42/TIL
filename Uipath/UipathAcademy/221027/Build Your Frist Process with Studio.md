## ****Building the Workflow—Part Two****

2단계 - 인보이스에 discount value 적기

### Workflow 만들기

1. 저장된 인보이스 파일의 인보이스 시트의 E8셀의 값을 변수 ClientCode에 저장한다.
    
    ![First.Name 은 해당 경로가 없으면 새로 생성하라는 뜻](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bdc352ff-515c-4a6e-ba86-a617e19c3cb9/Untitled.png)
    
    First.Name 은 해당 경로가 없으면 새로 생성하라는 뜻
    
    ⚠️ 오류발생!!
    
    ![E8 셀의 값이 string 형식으로 변환되지 않는다는 뜻](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a426aa5a-5e05-43cb-9534-ecc297273533/Untitled.png)
    
    E8 셀의 값이 string 형식으로 변환되지 않는다는 뜻
    
    → ClientCode의 형식을 Double로 바꿔준다.
    

1. [https://acme-test.uipath.com/first-automation](https://acme-test.uipath.com/first-automation) 페이지의 Part2를 클릭한 후 ClientCode를 입력하고 화살표를 클릭한다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/686af9c0-b609-4225-87b6-bbc317760366/Untitled.png)
    

1. 화면에 나온 Discount 값을 추출한 후 인보이스파일의 E18 셀에 입력한다.
    
    ![값이 안나오고 할인받지 못하는 Client라고 뜰 때도 있다.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3d5b2fc7-8b2f-4cb0-98af-db3d79536567/Untitled.png)
    
    값이 안나오고 할인받지 못하는 Client라고 뜰 때도 있다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1106aa23-f381-47ec-8a40-353b0462969b/Untitled.png)
    

1. 인보이스파일의 A31셀에 시그니처를 입력한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cf883554-619e-4baf-80ff-9e850ffae6a2/Untitled.png)

1. 완료
    
    ![discount 받는 경우](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1cd5acef-1d55-41b8-9ca9-c11f586d9c26/Untitled.png)
    
    discount 받는 경우
    
    ![discount 못받는 경우](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/924bd57e-8ea1-45e8-865e-d6540e1ed442/Untitled.png)
    
    discount 못받는 경우
    

---

## ****Building the Workflow—Part Three****

3단계 - 업데이트한 인보이스 파일을 첨부한 메일 보내기

### Workflow 만들기

1. 위처럼 값이 없는 경우를 대비해서 write cell을 if안에 넣어주고 경우를 구분한다.
    
    ![DiscountValue가 $를 포함하면 할인을 받는 경우이다.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3b512b38-3b82-43d6-ae1b-b34aa940650e/Untitled.png)
    
    DiscountValue가 $를 포함하면 할인을 받는 경우이다.
    

1. 시그니처 적는 부분을 이 다음으로 옮겨주고 메일을 작성한다.
(Use Desktop Outlook App 안에 Send Email 액티비티 사용)

![이렇게 하면 저 폴더 내의 모든 파일이 전송된다.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/949c0931-1bec-4437-adf2-debfa6821793/Untitled.png)

이렇게 하면 저 폴더 내의 모든 파일이 전송된다.

1. 메일을 확인하라는 메세지 박스를 띄우면 완료
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1cdcf7b9-ca32-425e-974b-a29e47ecdd90/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0ec1e421-11c4-4e09-a5a2-773875a1bf96/Untitled.png)
    
    ---
    
    ## ****Publishing and Running a Process****
    
    > 프로젝트 게시하고 어시스턴트 실행하기
    > 
    - 프로젝트 패널에서 특정 파일을 우클릭 후 게시에서 무시를 선택하면 게시된 패키지에서 생략할 수 있다.
    - project.json 파일이 읽기 전용 위치에 있는 경우 자동화 프로젝트를 게시할 수 없다.
    1. 우측 상단의 “게시” 버튼을 누른 후 패키지 이름, 버전, 정보를 입력한다.
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/86d0961a-818a-4286-ad96-54128bc5325f/Untitled.png)
        
    2. 게시 옵션은 개인 작업 영역 피드로 한 후 게시를 누른다.
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d832c805-8110-4a87-aa64-0518953176ee/Untitled.png)
        
    3. 어시스턴트를 켠 후 오케스트레이터와 연결한다.
    4. 실행
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5e7740e4-bbe9-460c-92a3-0065854c088e/Untitled.png)
        
    5. 오케스트레이터에서도 확인 할 수 있다.
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6e4c990a-1e5a-4160-95ca-9e698d9a899d/Untitled.png)
        
    
    ---
    
    <aside>
    📂<a href ="https://determined-fan-807.notion.site/Build-Your-Frist-Process-with-Studio-afab4b312c53469d84c4e78fddf28237">Notion</a>
    </aside>
