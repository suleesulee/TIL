#include<cstdio>
#include<cstring>

#define MAX 100
using namespace std;

int dx[] = {0, 1, 0, -1};
int dy[] = { 1, 0, -1, 0 };
int m, n;
int ans = 0;
int map[MAX][MAX];

void print_map() {
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			printf("%d ", map[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

int main() {
	memset(map, 0, sizeof(map));
	scanf("%d %d", &m, &n);

	map[0][0] = 1;
	int k = 0;
	int x = 0; 
	int y = 0;
	int check_cnt = 1;

	while (1) {
		int nx = x + dx[k];
		int ny = y + dy[k];
		if (0 <= nx && nx < m && 0 <= ny && ny < n && map[nx][ny] == 0) {
			map[nx][ny] = 1;
			x = nx;
			y = ny;
			check_cnt++;
		}
		else {
			ans++;
			if (k < 3)
				k++;
			else
				k = 0;
		}
		if (check_cnt == m * n) {
			break;
		}
		print_map();
		printf("ans: %d\n\n", ans);
	}


	printf("%d", ans);
}