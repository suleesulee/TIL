//뱀머리관련하여 다음 칸으로 이동하는 방법에 대해 구하기
//뱀의 위치들 기록

#include<cstdio>
typedef struct order {
	int x;
	char c;
}order;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0 , 0 };

int sec = 0;
int n, k, l;
int apple_x, apple_y;
order info[100];
int map[101][101] = { 0 };
int snake_dir = 1; // 1: 동 2:남 3: 서 4: 북
int snake_locate[100][2];

bool range_chk() {
	int nx = x + dx[];
	int ny = y + dy[];

	if (map[nx][ny] == 1 || (0 < nx && nx <= n) || (0 < ny && ny <= n)) {
		return false;
	}
	else
		return true;
}


void solve(){
	int snake_tail_x = 1;
	int snake_tail_y = 1;
	int map[1][1] = 1;
	snake_locate[0][0] = 1;
	snake_locate[0][1] = 1;
	bool chk;

	//다음위치에 몸통, 벽 확인
	chk = range_chk(snake_dir);
	
	//종료 조건이면 종료 아니면 계속 수행
	if (chk == false)
		printf("%d", sec);
	else {
		int nx = x + dx[];
		int ny = y + dy[];
		//다음위치에 사과?
		//있으면 사과 없어지고 해당 위치를 뱀으로 바꾸고 뱀의 새로운 위치 추가 
		if (map[nx][ny] == 2 )
		{	
			map[nx][ny] = 1;
		}
		else { //없음 머리 위치 옮기고 뱀 위치를 하나 당기고 꼬리 있던 위치를 0으로 변경 뱀의 위치를 추가
			map[nx][ny] = 1;	//위치를 옮기고 뱀의 위치를 변경
			snake_tail_x;
			snake_tail_y;
		}

		//1회 시간 증가
		sec++;

		//방향 돌려야하니
		for (int i = 0; i < l; i++) {
			if (sec == info[i].x) {
				if (info[i].c == 'L') {	//왼쪽으로 90
					if (snake_dir == 1) {
						snake_dir = 4;
					}
					else if (snake_dir == 2) {
						snake_dir = 1;
					}
					else if (snake_dir == 3) {
						snake_dir = 2;
					}
					else {
						snake_dir = 3;
					}
				}
				else {		//오른쪽으로 90
					if (snake_dir == 1) {
						snake_dir = 2;
					}
					else if (snake_dir == 2) {
						snake_dir = 3;
					}
					else if (snake_dir == 3) {
						snake_dir = 4;
					}
					else {
						snake_dir = 1;
					}
				}
				break;
			}
		}
	}
}


int main() {
	scanf("%d", &n);
	scanf("%d", &k);
	
	for (int i = 0; i < k; i++) {
		scanf("%d %d", &apple_x, &apple_y);
		map[apple_x][apple_y] = 2;
	}

	scanf("%d", &l);
	
	for (int i = 0; i < l; i++) 
		scanf("%d %c", &info[i].x, &info[i].c);
	
	solve();



	return 0;
}