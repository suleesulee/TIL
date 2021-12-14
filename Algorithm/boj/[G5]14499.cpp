#include<cstdio>

int dx[5] = { 0, 0, 0, -1, 1 };
int dy[5] = { 0, 1, -1, 0, 0 };

int n, m, x, y, k;
int map[20][20] = { 0 };
int order[1000] = { 0 };

typedef struct dice{
	int locate;
	int number;
}dice;

//0 바닥, 1 위, 2 북, 3 남, 4 동, 5 서
dice dice_status[6] = { {6,0}, {1,0}, {2,0}, {5,0}, {3,0}, {4,0} };

bool range_chk(int order) {
	int nx = x + dx[order];
	int ny = y + dy[order];
	
	if (0 <= nx && nx < n && 0 <= ny && ny < m) {
		return true;
	}
	return false;
}

void dice_change(int order) {
	int tmp;
	if (order == 1) 
	{
		tmp = dice_status[0].number;
		dice_status[0].locate = 3; 
		dice_status[0].number = dice_status[4].number;
		dice_status[4].locate = 1; 
		dice_status[4].number = dice_status[1].number;
		dice_status[1].locate = 4; 
		dice_status[1].number = dice_status[5].number;
		dice_status[5].locate = 6; 
		dice_status[5].number = tmp;
	}
	else if(order == 2) {
		tmp = dice_status[0].number;
		dice_status[0].locate = 4; 
		dice_status[0].number = dice_status[5].number;
		dice_status[5].locate = 1; 
		dice_status[5].number = dice_status[1].number;
		dice_status[1].locate = 3; 
		dice_status[1].number = dice_status[4].number;
		dice_status[4].locate = 6; 
		dice_status[4].number = tmp;
	}
	else if (order == 3)
	{
		tmp = dice_status[3].number;
		dice_status[3].locate = 6;
		dice_status[3].number = dice_status[0].number;
		dice_status[0].locate = 2; 
		dice_status[0].number = dice_status[2].number;
		dice_status[2].locate = 1; 
		dice_status[2].number = dice_status[1].number;
		dice_status[1].locate = 5; 
		dice_status[1].number = tmp;
	}
	else
	{
		tmp = dice_status[0].number;
		dice_status[0].locate = 5; 
		dice_status[0].number = dice_status[3].number;
		dice_status[3].locate = 1; 
		dice_status[3].number = dice_status[1].number;
		dice_status[1].locate = 2; 
		dice_status[1].number = dice_status[2].number;
		dice_status[2].locate = 6; 
		dice_status[2].number = tmp;
	}
}

void move_dice(int order) {

	if (range_chk(order)) {
		//주사위를 움직여서(현재 x,y 값 변경) 
		//조건에 맞춰 주사위상태, 맵 변경
		//윗면 출력
				
		x += dx[order];
		y += dy[order];
		
		dice_change(order);
		if (map[x][y] == 0) {
			map[x][y] = dice_status[0].number;
		}
		else {
			dice_status[0].number = map[x][y];
			map[x][y] = 0;
		}
		
		printf("%d\n", dice_status[1].number);
	}
	else {	
	}
}


int main() {

	scanf("%d %d %d %d %d", &n, &m, &x, &y, &k);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &map[i][j]);
		}
	}
	for (int i = 0; i < k; i++) {
		scanf("%d", &order[i]);
	}
	for (int i = 0; i < k; i++) {
		move_dice(order[i]);
	}
	return 0;
}

/*삼성문제였다고 한다
혼자풀었는데 답을 구현하는데 상당히 머릿속을 어지럽게하였다..
너무오래걸림.. 한문제에 3시간을 다쓸듯 집중의 차이가 있겠지만 이것만 집중해도 2시간은 걸릴듯 게다가
골드5문제다 평균 골드2,3으로 출제되는 경향이니 속도를 올릴 필요가 있고
써보면서 생각을 하는게 상당히 도움을 준다 꼭 써보며 해보기
*/