import itertools
def solution(numbers):
    answer = ''
    sum = []
    arrs = []
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    
    numbers.sort(key = lambda x : x*3, reverse=True)
    #print(numbers)
    
    
    return str(int(''.join(numbers)))


'''
Level2
Sort

문자열과 숫자형의 정렬비교 문제인데
처음에 permatuation으로 가려했다가 시간초과로 답을 확인함
3자리수라는걸로.. 문제에 힌트를 준것
333
303030
이러면 문자열에서는 333이 앞에오게됨
그리고 가장 큰수를 만들려면 3이 앞에와야 함

개인적으로 이런문제 좋아하지 않는다.


'''