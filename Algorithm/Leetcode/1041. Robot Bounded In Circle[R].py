'''
이 문제에서 중요한 점 2가지
1.방향 전환에 관련된 계산 모듈러4
2.한바퀴 돈 dir이 0(북쪽, 다른 경우는 시작방향)이 아니면 언젠간 탐험하다가 돌아온다는 이론(?)..

사실 이론이 아직도 이해가 잘안된다. 한바퀴 돌았을때 시작에서 바라보던 방향이 아니면 계속이동하다가 원점으로 돌아온다는 이야기라는데.. 모르겠다..
반복해서 어떻게 돌아올수있는가에 대해서 상당히 오랜시간 고민하다
답을 봤지만 명쾌한 해답은 아니었다.. 내가 이해력이 부족한 것일지도..
'''

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        robot_move = [[0,1],[1,0],[0,-1],[-1, 0]]
        robot_dir = 0 # 0:북 1: 동 2: 남 3: 서
        robot_x, robot_y = 0, 0
        for i in instructions:
            if i == 'G':
                robot_x += robot_move[robot_dir][0]
                robot_y += robot_move[robot_dir][1]
            elif i == 'L':
                robot_dir = (robot_dir + 3) % 4
            
            elif i == 'R':
                robot_dir = (robot_dir + 1) % 4
        
        
        return (robot_x == 0 and robot_y ==0) or robot_dir != 0
         