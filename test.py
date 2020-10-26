allZaego = {}
checker = 1

while checker:
    checker = int(input("0:종료, 1:항목추가, 2:재고확인 : "))
    if checker==1:
        print("항목 추가를 선택하셨습니다.")
        name = input("품목명 : ")
        plusMinus = int(input("1:매입, 2:매출 : "))
        if plusMinus ==1:
            print("매입을 선택하였습니다.")
        elif plusMinus ==2:
            print("매출을 선택하였습니다.")
        count = int(input("수량 : "))
        if plusMinus==2:
            count = -count
        exist = allZaego.get(name)
        if exist :
            zaego = exist + count
            allZaego[name]=zaego
        else:
            allZaego[name]=count
        print(name+"의 재고량 : ", end='')
        print(allZaego[name], end='\n\n')
    elif checker==2:
        print("재고 확인을 선택하셨습니다.")
        name = input("품목명 : ")
        print(name+"의 재고량 : ", end='')
        print(allZaego[name], end='\n\n')
    elif checker==0:
        print('프로그램 종료를 선택하셨습니다.')
    else:
        print("잘못 입력하셨습니다.")
