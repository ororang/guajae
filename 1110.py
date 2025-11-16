# 1번
# for i in range(1,10):
#     for j in range(1,10):
#         print(i,'*',j , '=', i*j - 1)
#     print('')

# 2번
# work = True
# total = 0
# a = input("성적을 입력하시겠습니까? (y/n)")
# if (a != 'y') and (a != 'n'):
#     print("잘못된 입력입니다.")
#     work = False
# elif a == 'n':
#      work = False

# while work:
#         b = input("원하는 교과목을 5가지 입력해주세요 예)국어 수학 영어 사회 과학")
#         subject = b.split()
#         for i in range(len(subject)):
#             score = int(input(f"{subject[i]} 점수를 입력해주세요"))
#             print(score,'점')
#             total += score
#         print('총 점수 : ',total)
#         print('평균 점수 : ', int(total/len(subject)))
#         break

# 3번
# list1 = ['1','2','3','4','5']
# s1 = '-'.join(list1)
# print(s1)

# dict1 = {'apple' : '사과', 'grape' : '포도', 'peach' : '복숭아'}
# print('-'.join(dict1))

# # list2 = [1,2,3,4,5]
# # print('-'.join(list2))

# s2 = '아 수업 언제 끝나지 아 집 가고 싶다 아 놀고 싶다 아 군대 가기 싫다'
# list3 = s2.split()
# print(list3)
# s3 = '아-수업-언제-끝나지-아-집-가고-싶다-아-놀고-싶다-아-군대-가기-싫다'
# list4 = s3.split('-')
# print(list4)
# print(s3.split('-',1))
# print(s3.split('-',2))
# s4 = '아\n수업\n언제\n끝나지\n아\n집\n가고\n싶다\n아\n놀고\n싶다\n아\n군대\n가기\n싫다'
# print(s4.splitlines())
