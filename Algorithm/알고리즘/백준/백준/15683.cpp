#include<cstdio>
#include<cstring>

using namespace std;

int n, m;
int map[8][8];
int memory_x[8];
int memory_y[8];
int memory_kind[8];
int m_cnt = 0;
int res = 99999999;


void print_map() {
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			printf("%d ", map[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

void cctv_cover(int dir, int x, int y) {
	if (dir == 0) {			//ºÏ
		int nx = x - 1;
		if (nx < 0)
			return;
		for (int j = nx; j >= 0; j--) {
			if (map[j][y] == 6)
				break;
			else if (map[j][y] != 0)
				continue;
			else
				map[j][y] = 7;
		}
	}
	else if (dir == 1) {	//µ¿
		int ny = y + 1;
		if (ny > m-1)
			return;
		for (int j = ny; j < m; j++) {
			if (map[x][j] == 6)
				break;
			else if (map[x][j] != 0)
				continue;
			else
				map[x][j] = 7;
		}
	}
	else if (dir == 2) {	//³²
		int nx = x + 1;
		if (nx > n-1)
			return;
		for (int j = nx; j < n; j++) {
			if (map[j][y] == 6)
				break;
			else if (map[j][y] != 0)
				continue;
			else
				map[j][y] = 7;
		}
	}

	else if (dir == 3) {	//¼­
		int ny = y - 1;
		if (ny < 0)
			return;
		for (int j = ny; j >= 0; j--) {
			if (map[x][j] == 6)
				break;
			else if (map[x][j] != 0)
				continue;
			else
				map[x][j] = 7;
		}
	}
}

void solve(int idx) {
	if (idx == m_cnt) {
		//print_map();
		int cnt = 0;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == 0)
					cnt++;
			}
		}
		if (res > cnt) {
			res = cnt;
		}
		return;
	}

	int c_map[8][8];

	if (memory_kind[idx] == 1) {
		for (int j = 0; j < 4; j++) {
			memcpy(c_map, map, sizeof(map));
			cctv_cover(j, memory_x[idx], memory_y[idx]);
			solve(idx + 1);
			memcpy(map, c_map, sizeof(map));
		}
	}
	else if (memory_kind[idx] == 2) {
		for (int j = 0; j < 2; j++) {
			memcpy(c_map, map, sizeof(map));
			cctv_cover(j, memory_x[idx], memory_y[idx]);
			cctv_cover(j + 2, memory_x[idx], memory_y[idx]);
			solve(idx + 1);
			memcpy(map, c_map, sizeof(map));
		}
	}
	else if (memory_kind[idx] == 3) {
		for (int j = 0; j < 4; j++) {
			memcpy(c_map, map, sizeof(map));
			cctv_cover(j, memory_x[idx], memory_y[idx]);
			cctv_cover((j + 1) % 4, memory_x[idx], memory_y[idx]);
			solve(idx + 1);
			memcpy(map, c_map, sizeof(map));
		}
	}
	else if (memory_kind[idx] == 4) {
		for (int j = 0; j < 4; j++) {
			memcpy(c_map, map, sizeof(map));
			cctv_cover((j + 2) % 4, memory_x[idx], memory_y[idx]);
			cctv_cover(j, memory_x[idx], memory_y[idx]);
			cctv_cover((j + 1) % 4, memory_x[idx], memory_y[idx]);
			solve(idx + 1);
			memcpy(map, c_map, sizeof(map));
		}
	}
	else if (memory_kind[idx] == 5) {
		memcpy(c_map, map, sizeof(map));
		cctv_cover(0, memory_x[idx], memory_y[idx]);
		cctv_cover(1, memory_x[idx], memory_y[idx]);
		cctv_cover(2, memory_x[idx], memory_y[idx]);
		cctv_cover(3, memory_x[idx], memory_y[idx]);
		solve(idx + 1);
		memcpy(map, c_map, sizeof(map));
	}
}


int main() {
	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &map[i][j]);
			if (map[i][j] != 6 && map[i][j] != 0) {
				memory_x[m_cnt] = i;
				memory_y[m_cnt] = j;
				memory_kind[m_cnt] = map[i][j];
				m_cnt++;
			}
		}
	}

	solve(0);
	printf("%d", res);
	
	return 0;
}