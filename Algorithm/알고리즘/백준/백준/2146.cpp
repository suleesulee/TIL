#include<cstdio>
#include<queue>

using namespace std;


int n;
int map[101][101] = { 0, };
int visit[101][101] = { 0, };
int color = 1;
int dx[4] = { 0 ,1, 0 ,-1 };
int dy[4] = { 1, 0, -1, 0 };
int ans[3];
int cnt = 0;
queue<pair<int, int>> q;

void bfs() {
	
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int k = 0; k < 4; k++) {
			int nx = dx[k] + x;
			int ny = dy[k] + y;
			
			if ((0 <= nx && nx < n) && (0 <= ny && ny < n)) {
				if (map[nx][ny] == 1 && visit[nx][ny] == 0) {
					q.push(make_pair(nx, ny));
					visit[nx][ny] = color;
				}
			}
		}
	}
}


void ans_bfs() {
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int k = 0; k < 4; k++) {
			int nx = dx[k] + x;
			int ny = dy[k] + y;

			if ((0 <= nx && nx < n) && (0 <= ny && ny < n)) {
				if (visit[x][y] == color){
					if (visit[nx][ny] == 0) {
						q.push(make_pair(nx, ny));
						visit[nx][ny] = color;
 					}
					if (visit[nx][ny] != color && visit[nx][ny] != 0) {
						ans[color - 1] = cnt;
						return;
					}
				}
			}
		}
		cnt++;
	}
}


int main() {
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &map[i][j]);
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (map[i][j] == 1 && visit[i][j] == 0) {
				q.push(make_pair(i, j));
				visit[i][j] = color;
				bfs();
				color++;
			}
		}
	}

	memcpy(map, visit, sizeof(map));

	color = 1 ;

	//for (int k = 0; k < 3; k++) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (visit[i][j] == color) {
					q.push(make_pair(i, j));
					ans_bfs();
				}
			}
		}

		//color++;
	//}




	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			printf("%d ", visit[i][j]);
		}
		printf("\n");
	}

}