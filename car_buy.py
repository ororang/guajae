print("예산은 2000만원입니다")
print("후보를 정해봅시다")


while(True):
    car_num = int(input("1. 기아 모닝 2. 기아 k5 3.기아 스포티지 4.기아 카니발"))
    if(car_num > 4 and car_num < 1):
        print("Invalid Input")
    selection = input("이 차로 고르시겠습니까? yes/no")


    if(selection == "yes"):
        print("구매방식을 고르겠습니다")
        buybuy = int(input("1. 신차 구매 2. 중고차 구매 3. 랜트"))
        if(buybuy > 0 and buybuy < 4):
            buy_selection = input("이 방식으로 구매하시시겠습니까? yes/no")
            if(buy_selection == "yes"):
                print("구매 완료했습니다")
                break
            else:
                continue
        else:
            print("invaild Input")
    if(selection != "no"):
        print("Invailt Input")
    else:
        continue
