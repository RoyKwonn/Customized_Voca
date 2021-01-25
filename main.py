# -*- coding: utf-8 -*-
import openpyxl
import random
import os

# 데이터 읽어와 리스트에 넣기
def read_xlsx(sheet):
    data = []
    for row in sheet.rows:
        word = []
        for j in range(2):
            word.append(row[j].value)
        word.append(int(row[2].value))
        data.append(word)

    return data

if __name__ == '__main__':

    # 엑셀파일 열기
    file = os.getcwd() + "/voca.xlsx"
    book = openpyxl.load_workbook(filename=file, read_only=False, data_only=False)

    # sheet1 불러오기
    # 데이터 읽어와 리스트에 넣기
    data = read_xlsx(book.worksheets[0])

    max_rows = len(data)
    # 점수
    score = 0

    # 테스트
    count = 0
    # 1, 2, 3 고르기

    # 몇 문제를 풀 것인지
    q_num = int(input("몇 문제를 푸시겠습니까? : "))
    q_list = random.sample(range(0, len(data)), q_num)


    while(count < q_num):
        print("\n")
        count += 1

        i = q_list.pop()

        # 보기
        select = []
        select.append(data[i])
        # 틀린 보기 만들기

        a = random.sample(range(0,len(data)),4)
        if i in a:
            a.remove(i)
        select.append(data[a[0]])
        select.append(data[a[1]])
        select.append(data[a[2]])
        random.shuffle(select)

        print(data[i][0])
        print("[1] " + select[0][1])
        print("[2] " + select[1][1])
        print("[3] " + select[2][1])
        print("[4] " + select[3][1])
        answer = int(input("번호 : ")) - 1

        # 정답인 경우
        if select[answer][1] == data[i][1]:
            print("정답입니다!")
            score += 1
            # 가중치 변경
            data[i][2] -= 1
            if data[i][2] < 1:
                print(data.pop(i))
        # 오답인 경우
        else:
            print("오답, 정답은 " + data[i][1])
            data[i][2] += 1

    # 테스트 종료
    print("\n\n%d개를 맞추었습니다." %(score))
    print("당신의 점수는", "%.2f" %((score*100)/count) + "점 입니다.")
    x = input("\n\nEnter 누르면 종료됩니다.")

    x = input("\n종료하고 싶으시면 Enter를 눌러주세요")
    # update 엑셀
    for n in range(1, len(data)):
        book.worksheets[0].cell(row=n, column=1).value = data[n-1][0]
        book.worksheets[0].cell(row=n, column=2).value = data[n-1][1]
        book.worksheets[0].cell(row=n, column=3).value = data[n-1][2]

    for n in range(len(data), len(data) - max_rows):
        book.worksheets[0].cell(row=n, column=1).value = ' '
        book.worksheets[0].cell(row=n, column=2).value = ' '
        book.worksheets[0].cell(row=n, column=3).value = ' '

    book.save(file)

