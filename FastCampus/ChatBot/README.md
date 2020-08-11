챗봇(ChatBot)이란?
===================

### 정의

    - 고객의 요청을 대신 응답해주는 채팅로봇
    - 사용자와 대화를 나눌수 있는 컴퓨터 프로그램
    - input -> process -> output
    - 텍스트, 음성(자연어) 등을 입력 받아서 가장 적절한 답변을 출력
    - AI가 있고 없는 챗봇이 있음

### 챗봇에 관심을 갖게된 배경

    - 메신저 이용자 증가
    - 자연어처리 기술 혁신
    - AI 기술의 발전

### 챗봇 관련 용어

    - 자연어
    - 자연어 처리(NLU: Natural Language Understanding)
    - 자연어처리 엔진(자연어처리를 해주는 툴들을 얘기함 ex) 챗봇빌더: 구글 Dialogflow, IBM 왓슨, Facebook wit ai)
    - 인텐트(Intent) : 인간이 한 말 또는 의도를 이해하는 것 
    - 대화문장, 말뭉치(Utterance) <= 이와 같은 훈련데이터를 미리 준비해야함
    - 엔티티(Entity) : 명사에 해당
    - 시나리오 : 설계된 대화의 흐름
    - 슬롯 채우기(slot filling) : 날씨를 물어보면 온도, 미세먼지 등등 정보들을 채움으로써 적절한 응답을 해줌
    - 스몰토크(Smalltalk) : 일상의 대화
    - 자연어 생성(NLG: Natural Language Generation) : 규칙에 의하거나 마구잡이(인공지능)로 하거나 등등

### Dialogflow
    
    - 구글에서 만든 챗봇빌더로 코딩없이 쉽게 만들 수 있다.
    - Users=>APP/DEVICE=>API.AI PLATFORM=>INTENT=>ACTIONABLE DATA=>OUTPUT의 흐름으로 진행됨
    - INTENT<=>FULFILLMENT(DB나 EXTERNAL APIs)
    - https://dialogflow.cloud.google.com/#/getStarted

### 
