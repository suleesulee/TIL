def solution(places):
    answer = []
    ans = -1   
    
    def check(wait, x, y):
        dx1 = [1, 0, 0, -1]
        dy1 = [0, 1, -1, 0]
        dx2 = [1, 1, -1, -1]
        dy2 = [-1, 1, 1, -1]
        
        #상하 좌우 확인
        for i in range(4):
            nx = x + dx1[i]
            ny = y + dy1[i]
            
            if 0 <= nx and nx < 5 and  0 <= ny and ny < 5:
                if places[wait][nx][ny] == 'P':
                    return 0
        #상하 좌우 +2범위 확인 해당 범위 앞에 가림막 있으면 OK 아닐경우 0
        for i in range(4):
            nx = x + (dx1[i] * 2)
            ny = y + (dy1[i] * 2)
            fx = x + dx1[i]
            fy = y + dy1[i]
            
            if 0 <= nx and nx < 5 and 0 <= ny and ny < 5:
                if places[wait][nx][ny] == 'P' and places[wait][fx][fy] != 'X':
                    return 0
        
        #대각선 확인
        for i in range(4):
            nx = x + dx2[i]
            ny = y + dy2[i]
            
            if 0 <= nx and nx < 5 and  0 <= ny and ny < 5:
                if places[wait][nx][ny] == 'P':
                    if places[wait][nx][y] != 'X' or places[wait][x][ny] != 'X':
                        return 0
        return 1
        
    for k in range(5):
        for i in range(5):
            for j in range(5):
                if places[k][i][j] == 'P':
                    ans = check(k, i, j)
                    if ans == 0:
                        answer.append(ans)
                        break
            if ans == 0:
                break
        if ans != 0:
            answer.append(1)
        ans = -1
    

    
    return answer