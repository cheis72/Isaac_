# 숫자 야구 게임

N=int(input())   # 추리한 횟수

num_list=[1,2,3,4,5,6,7,8,9]

# answer_list 초기
answer_list=[]
for first in num_list:
    for second in num_list:
        for third in num_list:
            if first!=second and second!=third and first!=third:
                answer_list.append(first*100+second*10+third)

for i in range(N):
    guess_num, strike, ball = map(int, input().split())

    answer=[]
    for number in answer_list:
        count_strike=0
        count_ball=0
        for index in range(3):
            if str(guess_num)[index]==str(number)[index]: count_strike+=1
            elif str(guess_num)[index] in str(number): count_ball+=1
        if count_strike==strike and count_ball==ball: answer.append(number)
    answer_list=answer

print(len(answer_list))
