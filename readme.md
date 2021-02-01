# Customized_Voca

## 추가하고 싶은 기능

1. 문제 풀이 타이머
2. GUI
3. 진행사항(퍼센트)
4. 앱으로도 구현
5. 어휘 입력
6. heap / 날짜 / 랜덤 을 비율로 문제 출제하
7. 숫자가 아닌 입력시 재입력 요청
8. 입력 후 멈추기 (정답이 입력 옆에 나오기)

## 진행사항

- .xlsx 파일 열기
- data 읽어오기
- 몇 문제 풀지 고르기
- 문제 풀기
	- 보기 만들기
	- 정답인 경우
		- 가중치 - 1
		- 만약 가중치가 0이 된다면 data에서 삭제
	- 오답인 경우
		- 가중치 + 1
- 엑셀에 변경사항 update하기
- 얼마나 풀이햐였는지 보여주기


## 구성조건

### 1차 목적
- (default of 가중치 : 3)
- xxx.xlsx에서 단어, 뜻, 예문, 가중치 읽어오기  
- heap1에 저장 후, 불러온 문제 틀릴때마다 가중치 올려주기(맞추면 내리기) 이때 새로운 heap2에 저장시킨다.
- 가중치가 0가 된것들은 삭제한다
- 변경된 사항을 다시 xlsx에 저장한다.

### 2차 목적 - 1
- python을 서버로 변화시킨다.
- heap에서 꺼낸 걸 client에 보내고 응답을 기다린다.
- 1차 목적처럼 처리한다.

### 2차 목적 - 2
- IOS 어플 안에서 단어, 뜻, 예문을 입력시킨다.
- 입력사항을 json을 저장시킨다.
- IOS 안에서 알고리즘을 처리한다.
- IOS app 
