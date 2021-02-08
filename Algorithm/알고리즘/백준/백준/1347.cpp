#include<cstdio>
#include<cstring>

using namespace std;

int n;
char note[50];
char dummy;
int map[101][101];

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1 ,0, -1 };
int dir = 2;//south

int x=50, y=50;

void t_R(int d) {
	if (d != 3)
		dir += 1;
	else
		dir = 0;
}
void t_L(int d) {
	if (d != 0)
		dir -= 1;
	else
		dir = 3;
}
void make_map(int dir) {
	x = x + dx[dir];
	y = y + dy[dir];
	map[x][y] = 1;
}

int main() {
	memset(map, 0, sizeof(map));
	map[x][y] = 1;

	scanf("%d", &n);
	scanf("%1c", &dummy);
	for (int i = 0; i < n; i++) {
		scanf("%1c", &note[i]);
	}

	for (int i = 0; i < n; i++) {
		if (note[i] == 'R') {
			t_R(dir);
		}
		else if (note[i] == 'L') {
			t_L(dir);
		}
		else if (note[i] == 'F') {
			make_map(dir);
		}
	}

	int sx, sy, ex, ey;

	sx = sy = 101;
	ex = ey = 0;

	for (int i = 0; i < 101; i++) {
		for (int j = 0; j < 101; j++) {
			if (map[i][j] == 1) {
				if (i < sx) sx = i;
				if (j < sy) sy = j;
				if (i > ex) ex = i;
				if (j > ey) ey = j;
			}
		}
	}

	for (int i = sx; i <= ex; i++) {
		for (int j = sy; j <= ey; j++) {
			if (map[i][j] == 1) 
				printf(".");
			else 
				printf("#");
		}
		printf("\n");
	}




	return 0;
}