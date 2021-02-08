#include<cstdio>
#include<cstring>
#include<queue>
#include<vector>
#define MAX 101 

using namespace std;

int dx[] = { 0,1,0,-1 };
int dy[] = { 1,0,-1,0 };

queue < pair<int, int>> q;

int map[MAX][MAX];
int h, w;
char cin;
int tc;
int prisoner1_x = -1;
int prisoner2_x = -1;
int prisoner1_y = -1;
int prisoner2_y = -1;

void print_map() {
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			printf("%d ", map[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

void init() {
	memset(map, 0, sizeof(map));
	prisoner1_x = -1;
	prisoner2_x = -1;
	prisoner1_y = -1;
	prisoner2_y = -1;
}

void bfs() {

	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (0 <= nx && nx < h && 0 <= ny && ny < w) {
				if (map[nx][ny] == 0 && visit[nx][ny] == 0)  {
					q.push({nx, ny});
					visit[nx][ny] = 1;
				}
			}
		}
	}

}


int main() {
	scanf("%d", &tc);
	for (int i = 0; i < tc; i++) {
		scanf("%d %d", &h, &w);
		getchar();
		// .공간 :0 *벽:1 #문:2 $죄수 :3
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				scanf("%1c", &cin);
				if (cin == '.')
					map[i][j] = 0;
				else if (cin == '*')
					map[i][j] = 1;
				else if (cin == '#')
					map[i][j] = 2;
				else if (cin == '$') {
					map[i][j] = 3;
					if (prisoner1_x == -1) {
						prisoner1_x = i;
						prisoner1_y = j;
					} else {
						prisoner2_x = i;
						prisoner2_y = j;
					}
				}
			}
			getchar();
		}


		//print_map();
		init();
	}
	
	return 0;
}