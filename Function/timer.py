import time

# !!!!!!!!! 문제 최대 풀이시간
sec = int(input("시간을 입력하시오(초) : "))

# while은 반복문으로 sec가 0이 되면 반복을 멈춰라
while(sec > 0):
    print(sec)
    time.sleep(1)
    sec = sec - 1

# !!!!!!!!!!!! 문제 풀이 평균 측정

# 타이머 시작점
start = input("Enter를 누르면 타이머를 시작합니다.")
begin = time.time()

# 타이머 종료점
stop = input("Enter를 누르면 측정을 종료합니다.")
end = time.time()

# 시간차
result = end - begin

# round는 파이썬에서 소수점 자리수 조절에 활용됩니다.
result = round(result, 3)
print("시작 후", result, "초의 시간이 흘렀습니다.")
