#include<cstdio>
#include<cstring>

using namespace std;

char in1;
int in2;
int in3;
int map[7][7];
int check[7][7];
int flag = 1;
int first_x, first_y;

int dx[] = { -2, -1, 1, 2, 2, 1, -1, -2 };
int dy[] = { 1, 2, 2, 1, -1, -2, -2, -1 };

int check_knight(int x, int y, int px, int py) {
	int nx, ny;
	int res = 0;
	for (int i = 0;i < 8;i++) {
		nx = px + dx[i];
		ny = py + dy[i];
		if (0 < nx && nx < 7 && 0 < ny && ny < 7) {
			if (x == nx && y == ny) {
				res = 1;
				break;
			}
		}
	}
	return res;
}

int change_v(int i) {
	if (i == 6) {
		return 1;
	}
	else if (i == 5) {
		return 2;
	}
	else if (i == 4) {
		return 3;
	}
	else if (i == 3) {
		return 4;
	}
	else if (i == 2) {
		return 5;
	}
	else if (i == 1) {
		return 6;
	}
	else {
		//err
		return -1;
	}
}

int change_ctoi(char c) {
	if (c == 'A') {
		return 1;
	}
	else if (c == 'B') {
		return 2;
	}
	else if (c == 'C') {
		return 3;
	}
	else if (c == 'D') {
		return 4;
	}
	else if (c == 'E') {
		return 5;
	}
	else {
		return 6;
	}
}

int check_map(int x, int y, int px, int py, int f)
{
	int res = 0;
	if (f == 1) {
		map[x][y] = 1;	//첫번째 진입
		first_x = x;
		first_y = y;
		return 0;
	}
	else {
		//이전꺼 나이트 경로 체크한뒤
		//체크된 경로에 x,y가 있으면 정답
		//아니면 인밸리드 리턴
		if (map[x][y] == 1) {	//방문한 경로를 방문
			return -1;
		}
		else {
			res = check_knight(x, y, px, py);
			if(res == 1)
				map[x][y] = 1;
			else {
				return -1;
			}
		}
	}
}

int last_to_first(int last_x, int last_y) {
	int res = 0;
	int nx, ny;
	for (int i = 0; i < 8; i++) {
		nx = last_x + dx[i];
		ny = last_y + dy[i];
		if (0 < nx && nx < 7 && 0 < ny && ny < 7) {
			if (first_x == nx && first_y == ny) {
				res = 1;
				break;
			}
		}
	}
	return res;
}

int main()
{
	int res;
	int r1, r2;
	memset(map, 0, sizeof(map));
	for (int i = 0; i < 36; i++) {
		scanf("%1c %1d", &in1, &in2);
		getchar();
		
		in3 = change_ctoi(in1);
		in2 = change_v(in2);
		
		res = check_map(in2, in3, r1, r2, flag);
		if (res == -1) {
			printf("Invalid");
			return 0;
		}
		r1 = in2;
		r2 = in3;
		flag = 0;

		if (i == 35) {
			res = last_to_first(in2, in3);
			if (res == 0) {
				printf("Invalid");
				return 0;
			}
		}
	}

	printf("Valid");
	return 0;
}