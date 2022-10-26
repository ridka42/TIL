# 10/26

# Build Your Frist Process with Studio

## Meet the Uipath Studio Interface

인터페이스 소개

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c2b16299-1d42-4460-b81c-3666363c9c92/Untitled.png)

Focus는 디버깅 중 오류를 일으킨 활동이나 현재 중단점으로 돌아갈 수 있도록 도와줍니다.

---

## Underatanding the Business Scenario

프로젝트 소개

1. 새 인보이스에 대한 Outlook 전자 메일 받은 편지함 폴더를 확인합니다.
2. 인보이스를 저장합니다.
3. 각 인보이스에서 클라이언트 코드를 찾아 저장합니다.
4. “ACME System 1” 웹페이지에 접속합니다.
5. 각 클라이언트 코드에 대한 할인 값을 가져옵니다.
6. 해당 인보이스에 할인 금액을 입력합니다.
7. 업데이트된 인보이스 파일을 포함하는 Outlook에서 초안 이메일을 준비합니다.

---

## ****Building the Workflow—Part One****

1단계 - ACME가 보낸 메일에 첨부된 파일 저장하기

### workflow 개발 전 고려 사항

- 무인 / 유인 로봇을 잘 골라야함. 나중에 바꾸려면 골치아프다.
- 프로젝트 레이아웃 (시퀀스, 플로차트, state 머신)을 잘 골라야함
- 필요한 종속성 설치 했는지
- **UiPath Automation Best Practice**

### Workflow 만들기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/476eb952-dc8a-47f9-9669-e6434885c443/Untitled.png)

1. outlook 메일을 불러옴 (*ridka4242@outlook .com)*
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/db5bb84e-7848-49cf-94df-d3ffa264e467/Untitled.png)
    
2. for each에 불러온 메일들이 담긴 변수를 넣고 반복문 돌림
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c42222ec-c483-4d5b-946d-ea5758c615c6/Untitled.png)
    
3. 메일마다 첨부파일을 저장하도록 한다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ab8d0d10-0956-43ae-b81f-c3fc28c474a7/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6ee00082-922d-4c8d-bd3e-2e054987d6a0/Untitled.png)
    
4. 완료

<aside>
📂 [1026FristProcess](https://github.com/ridka42/Uipath-Academy.git)

</aside>
