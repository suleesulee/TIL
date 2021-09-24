class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 방향이 같으면 절대 안만남 방향이 다른데 
        # 방향이 달라서 만나면 절대값이 큰게 이김
        
        ans = []
        
        for asteroid in asteroids:
            while ans and ans[-1] >= 0 and asteroid < 0:
                collision = ans[-1] + asteroid
                if collision <= 0:
                    ans.pop()
                if collision >= 0:
                    break
            else:
                ans.append(asteroid)
                    
        return ans

'''
Medium
Stack

복잡한 스택구현 문제
while, else 문이 존재한다는 것 처음 알았다 ㄷㄷ
구현하라는데로 구현하면 된다.

'''