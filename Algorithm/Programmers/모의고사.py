'''
수포자들이 찍는 방식과
답을 비교한다..
answers 의끝까지
'''

def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    cnt = []
    cnt1, cnt2, cnt3 = 0, 0, 0
    
    
    for i in range(3):
        if i == 0:
            for j in range(len(answers)):
                tmp = j
                if j >= 5:
                    tmp = j % len(s1)
                if answers[j] == s1[tmp]:
                    cnt1 += 1
            cnt.append(cnt1)
        if i == 1:
            for j in range(len(answers)):
                tmp = j
                if j >= len(s2):
                    tmp = j % len(s2)
                if answers[j] == s2[tmp]:
                    cnt2 += 1
            cnt.append(cnt2)
        if i == 2:
            for j in range(len(answers)):
                tmp = j
                if j >= len(s3):
                    tmp = j % len(s3)
                if answers[j] == s3[tmp]:
                    cnt3 += 1
            cnt.append(cnt3)
                    
    max_v = max(cnt1, cnt2, cnt3)
    
    #print(cnt)
    for i in range(3):
        if max_v == cnt[i]:
            answer.append(i+1)
    
    
    return answer