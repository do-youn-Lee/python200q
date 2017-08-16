from random import shuffle
from time import sleep
import xlrd


workbook = xlrd.open_workbook('lotto.xlsx')
worksheet = workbook.sheet_by_index(0)

xls_rows = worksheet.nrows

lotto = []
for rows in range(3, xls_rows):
    temp = []
    for cols in range(13, 19):
        temp.append(int(worksheet.cell_value(rows, cols)))
    # print(temp)
    lotto.append(temp)

gamenum = 15 # input('로또 게임 회수를 입력하세요: ')

for i in range(gamenum):
    balls = [x+1 for x in range(45)]
    ret = []
    for j in range(6):
        shuffle(balls)
        number = balls.pop()
        ret.append(number)
    ret.sort()
    if ret in lotto:
        i -= 1

    print('로또번호[%d]: ' %(i+1), end='')
    print(ret)
    sleep(1)
