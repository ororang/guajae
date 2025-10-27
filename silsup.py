# 18 <= age <= 25
# age >= 18 and age<=25
# sex =='male' and 18 <= age<= 25
# sex =='male' and age >= 18 and age <= 25
# kor >= 70 and eng >= 70 and math >= 70 or kor + eng + math >= 240
# age1 + age2 >=40 and age1 + age2 <= 40

# jumsu = int(input("점수 입력 :"))
# if jumsu >= 4.2:
#     print("당신의 평점은 :",jumsu)
#     print("해외연수 기회 부여")

# jumsu = float(input("점수 입력 :"))
# if jumsu >= 4.2:
#     print("당신의 평점은 :",jumsu)
#     print("해외연수 기회 부여")

# kor = int(input("국어 점수 입력 :"))
# eng = int(input("영어 점수 입력 :"))
# math = int(input("수학 점수 입력 :"))
# avg = (kor + eng + math) / 3
# if avg >= 95:
#     print("당신의 평균 점수는 :",avg)
#     print("장학금 지급 대상자입니다.")
# print("감사합니다")


# age = int(input())

# if age >- 65:
#     print("지하철 우대 승차권 발급")
# else:
#     print("지하철 일반 승차권 발급")

# print("자동 발매기를 이용해주셔서 감사합니다.")

# num1 = input("첫 번째 숫자 입력 :")
# num2 = input("두 번째 숫자 입력 :")

# if num1 > num2:
#     print("두 수 중에 큰수는 " + num1 + " 이고 작은수는 " + num2 + " 입니다.")
# else:
#     print("두 수 중에 큰수는 " + num2 + " 이고 작은수는 " + num1 + " 입니다.")

# num1 = int(input("첫 번째 숫자 입력 :"))
# num2 = int(input("두 번째 숫자 입력 :"))

# if num1 > num2:
#     print("두 수 중에 큰수는 " + num1 + " 이고 작은수는 " + num2 + " 입니다.")
# else:
#     print("두 수 중에 큰수는 " + num2 + " 이고 작은수는 " + num1 + " 입니다.")

# num1 = int(input("첫 번째 숫자 입력 :"))
# num2 = int(input("두 번째 숫자 입력 :"))

# if num1%2==0 and num2%2==0:
#     print("두 수는 짝수입니다.")
# elif num1%2!=0 and num2%2!=0:
#     print("두 수는 홀수입니다.")
# else:
#     print("한 수는 짝수이고 한 수는 홀수입니다.")


# socre = int(input("점수 입력 :"))
# if socre >= 90:
#     print("A학점")
# elif socre >= 80:
#     print("B학점")
# elif socre >= 70:
#     print("C학점")
# elif socre >= 60:
#     print("D학점")
# else:
#     print("F학점")


# socre = int(input("점수 입력 :"))

# if socre >= 60:
#     if socre >= 70:
#         if socre >= 80:
#             if socre >= 90:
#                 print("A학점")
#             else:
#                 print("B학점")
#         else:
#             print("C학점")
#     else:
#         print("D학점")
# else:
#     print("F학점")


# sub1 = int(input("첫 번째 과목 점수 입력 :"))
# sub2 = int(input("두 번째 과목 점수 입력 :"))
# total = sub1 + sub2
# if(sub1 >= 75) and (sub2 >= 75):
#     if total >= 180:
#         print("최우수 학생")
#     elif total >= 160:
#         print("우수 학생")
#     else:
#         print("보통 학생")
# else:
#     print("노력 필요 학생")


# sex = input("성별 입력 (남/여) :")
# height = float(input("키 입력 (cm) :")) / 100
# weight = float(input("몸무게 입력 (kg) :"))

# if(sex == "남"):
#     avg = (height * height) * 22
#     if 110 <= weight / avg * 100 <= 120:
#         print("표준 체중입니다.")
#     elif weight / avg * 100 < 110:
#         print("저체중입니다.")
#     else:
#         print("과체중입니다.")
# elif(sex == "여"):
#     avg = (height * height) * 21
#     if 110 <= weight / avg * 100 <= 120:
#         print("표준 체중입니다.")
#     elif weight / avg * 100 < 110:
#         print("저체중입니다.")
#     else:
#         print("과체중입니다.")
# else:
#     print("성별을 잘못 입력하였습니다.")

# month = int(input("월 입력 (1~12) :"))

# if((month < 1) or (month > 12)):
#     print("잘못된 입력입니다.")
# elif(month == 3) or (month == 4) or (month == 5):
#     print("봄입니다.")
# elif(month == 6) or (month == 7) or (month == 8):
#     print("여름입니다.")
# elif(month == 9) or (month == 10) or (month == 11):
#     print("가을입니다.")
# else:
#     print("겨울입니다.")


# level = int(input("직급 입력"))
# age = int(input("나이 입력"))

# if(((level == 7) or (level == 8)) and (40 <= age) and (age <= 50)):
#     print("연금 80% 지급 대상자입니다. ")
# elif((level == 9) and (50 <= age) and (age <= 60)):
#     print("연금 90% 지급 대상자입니다. ")
# elif((level == 10) and (age >= 60)):
#     print("연금 100% 지급 대상자입니다. ")
# else:
#     print("연금 지급 대상자가 아닙니다. ")


# age = int(input("나이 입력 :"))

# if age >=8:
#     height = int(input("키 입력 :"))
#     if height >= 120:
#         print("놀이기구 탑승이 가능합니다.")
#     else:
#         print("놀이기구 탑승이 불가능합니다.")
# else:
#     print("놀이기구 탑승이 불가능합니다.")


# num = int(input("정수 입력 :"))

# if(num < 0):
#     print("음수입니다.")

# if(num == 0):
#     print("0입니다.") 
# if(num > 0):
#     print("양수입니다.")


# num = int(input("정수 입력 :"))
# if(num <0):
#     print("음수입니다.")
# elif(num ==0):
#     print("0입니다.")
# else:
#     print("양수입니다.")


num1 = int(input("첫 번째 정수 입력 :"))
op = input("연산자 입력 (+, -, *, /) :")
num2 = int(input("두 번째 정수 입력 :"))

if(op == "+"):
    print("결과 :", num1 + num2)
elif(op == "-"):
    print("결과 :", num1 - num2)
elif(op == "*"):
    print("결과 :", num1 * num2)
elif(op == "/"):
    print("결과 :", num1 / num2)
else:
    print("잘못된 연산자입니다.")
