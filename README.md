
# [AI/빅데이터] 애널리스트 보고서, GPT로 한눈에 보기
  
**애널리스트는 다양한 시각이 담긴 정보를 보고서 형식으로 발간해 시장에 신속하게 제공하지만, 매주 1,170편가량 발간되는 보고서를 모두 살펴보기는 어렵습니다. 이에 GPT를 활용해 다량의 보고서에서 텍스트 컨센서스를 생성하는 방법을 소개합니다.

## I. 텍스트 컨센서스의 필요성

- 증권사 애널리스트가 발간하는 보고서는 투자자들에게 정보를 제공하는 역할을 수행한다. 

- 애널리스트의 실적 추정치는 실제 기업 실적 예측에 유의미하며, 더 많은 애널리스트가 추정할수록 예측의 정확도가 상승하는 경향이 있다. 

- 애널리스트들의 동일한 주제에 대한 다양한 시각도 투자판단에 유의미하다. 하지만, 일주일에 평균 1,170편가량 발간되는 보고서를 모두 확인하는 것은 불가능하다. 

- 애널리스트들의 의견을 취합한 텍스트 컨센서스를 생성할 수 있다면, 시장에 대한 정보를 한눈에 확인할 수 있을 것이다.

## II. GPT를 활용한 텍스트 컨센서스 생성

- 최근 GPT(Generative Pretrained Transformer)와 같은 LLM(대규모 언어모델)이 텍스트 생성 분야에서 뛰어난 성능을 보이고 있다. 이에 LLM을 사용하여 애널리스트의 보고서를 취합하고 텍스트 컨센서스를 생성하였다.

- 텍스트 컨센서스 생성 알고리즘은 우선 질문(Query)과 가장 잘 대응하는 보고서 내 내용을 취합한 후, 취합된 내용을 근거로 질문에 대한 대답을 출력하는 방식을 사용하였다. 

- 알고리즘 구동 결과, 애널리스트의 보고서에 존재하지 않는 내용에 대한 질문에는 답변이 제한적이었으나, 최근 금융시장과 관련한 거의 모든 질문에 대해서는 유효한 텍스트 컨센서스를 답변으로 생성했다.

# 
# <a border="0" href="http://tracking.nhqv.com/tracking?SITE_ID=4&SEND_ID=3980109&SCHD_ID=2977176&WORKDAY=20230426&TRACKING_CLOSE=2023-04-19&TYPE=C&CLICK_ID=002&MEMBER_ID=a3lvdWppbi5raW1Abmhxdi5jb20=&MEMBER_ID_SEQ=32958&URL=https://download.nhqv.com/www/plugin/pdfjs/web/viewer.html?r=CommFile&p=/cis/rsh/inv&i=CISPPR20230417155400047" target="_blank" title="NH 리서치 원문보기"><img border="0" src="https://www.nhqv.com/img/ems/research/img_09.jpg"></a>

<br/><br/>
# 어플리케이션 설치 및 실행
- [링크](https://github.com/kyoujinkim/ConsensusGPT_Application/tree/master)에서 어플리케이션 설치법 확인
