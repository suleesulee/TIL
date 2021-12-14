#include<cstdio>
#include<cstdlib>

int dx[] = { -1, -1, 0, 1, 1, 1, 0, -1 };
int dy[] = { 0, -1, -1, -1, 0, 1, 1, 1 };


int fish_dir[4][4];
int fish_num[4][4];
int shark_d;
int shark_cnt;
int shark_x, shark_y; 
int rotate = 1;

void print_test() {

	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			printf("%d %d ", fish_num[i][j], fish_dir[i][j]);
		}
		printf("\n");
	}

	printf("\n");

}

void init() {
	shark_d = fish_dir[0][0];
	shark_cnt = fish_num[0][0];
	shark_x = 0;
	shark_y = 0;
	fish_dir[0][0] = -1;
	fish_num[0][0] = -1;
}

void rotate_fnum()
{
	int x = 0;
	int y = 0;
	int i = 0;
	int j = 0;
	int temp_dir = -1;

	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (fish_num[i][j] == rotate) {
				temp_dir = fish_dir[i][j];
				x = i;
				y = j;
				break;
			}
		}
		if (temp_dir != -1)
			break;
	}

	//printf("%d\n", temp_dir);

	if (temp_dir != -1 && x + dx[temp_dir - 1] >= 0 && x + dx[temp_dir - 1] < 4 && y + dy[temp_dir - 1] >= 0 && y + dy[temp_dir - 1] < 4 && fish_num[x + dx[temp_dir - 1]][y + dy[temp_dir - 1]] != -1) {
		int nx = x + dx[temp_dir - 1];
		int ny = y + dy[temp_dir - 1];

		//printf("%d %d\n", nx, ny);

		int temp_fish_num = fish_num[nx][ny];
		int temp_fish_dir = fish_dir[nx][ny];

		fish_num[nx][ny] = fish_num[x][y];
		fish_dir[nx][ny] = fish_dir[x][y];

		fish_num[x][y] = temp_fish_num;
		fish_dir[x][y] = temp_fish_dir;
		rotate++;
		//printf("rota : %d\n", rotate);
	}
	else if (temp_dir == -1) {
		rotate++;
	}
	else{
		if(fish_dir[x][y] + 1 != 9)
			fish_dir[x][y] += 1;
		else 
			fish_dir[x][y] = 1;
	}


}

int move_shark() {
	//상어가 움직일수있음 1. 다음 타켓을 먹음 2. 기존에 있던자리를 움직일수있는 자리로 수정하고 새로운 자리에 마킹 
	if ((shark_x + dx[shark_d - 1] >= 0 && shark_x + dx[shark_d - 1] < 4) && (shark_y + dy[shark_d - 1] >= 0 && shark_y + dy[shark_d - 1] < 4)) {
		int nsx = shark_x + dx[shark_d - 1];
		int nsy = shark_y + dy[shark_d - 1];
		
		shark_cnt += fish_num[nsx][nsy];
		shark_d = fish_dir[nsx][nsy];

		fish_num[shark_x][shark_y] = 0;
		fish_dir[shark_x][shark_y] = 0;

		shark_x = nsx;
		shark_y = nsy;

		fish_num[nsx][nsy] = -1;
		fish_dir[nsx][nsy] = -1;

		return 1;
	}
	else //상어가 움직이는 곳이 사각형 밖 "끝"
		return 0;
}

int main() {

	//vector<pair<int, int>> v;

	int res;

	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			scanf("%d %d", &fish_num[i][j], &fish_dir[i][j]);
		}
	}

	init();

	while (1) {
		rotate_fnum();
		if (rotate == 17) {
			//break;
			rotate = 1;
			res = move_shark();
			break;
			//if (res == 0) {
			//	printf("%d", shark_cnt);
			//	break;
			//}

		}
		print_test();
	}

	print_test();

	return 0;
}