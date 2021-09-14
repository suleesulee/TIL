class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 처음 접근법 리스트에 넣고 빈도별로 정렬해서 쓰려고했음
        # 어느정도 맞는 접근법 그러나 그 방식을 사용하려면 조건문이 엄청남
        # 아래와 같음
        
        
        total = a + b + c
        a_cnt, b_cnt, c_cnt = 0, 0, 0
        s = ""
        
        for i in range(total):
            # a를 쓰려면 b,c 보다 a가 커야하고 cnt 가 2보다 크면안됨 3번 쓸수 없으니
            # b를 두번 썼는데 a를 쓸수있어야함 c를 두번썼는데 a가 쓸수있어야함
            if (a >= b and a>=c and a_cnt != 2) or (b_cnt == 2 and a > 0) or (c_cnt == 2 and a > 0):
                s += 'a'
                a-=1
                a_cnt += 1
                b_cnt = 0
                c_cnt = 0
            
            elif (b >= a and b >= c and b_cnt != 2) or (a_cnt == 2 and b > 0) or (c_cnt == 2 and b > 0):
                s += 'b'
                b_cnt += 1
                b -= 1
                a_cnt = 0
                c_cnt = 0
            elif (c >= a and c >= b and c_cnt != 2) or (a_cnt == 2 and c > 0) or (b_cnt == 2 and c > 0):
                s += 'c'
                c_cnt += 1
                c -= 1
                a_cnt = 0
                b_cnt = 0
            

        
        return s
    
'''
Medium
Greedy

미칠듯한 조건문을 타야 그리디한 답을 구할 수있다.
조건은 위에 써놨다.
가장큰거부터 소비하고 2개이상 들어가게되면 중간에 껴넣으려는 작업을 한다.



'''