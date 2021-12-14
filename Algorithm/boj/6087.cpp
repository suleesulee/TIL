#include<cstdio>
#include<queue>

using namespace std;

int w, h;
char map[101][101];
int visit[101][101];

int startx = -1;
int endx = -1;
int starty, endy;
char c;

int dx[4] = { 0,  1, 0, -1 };
int dy[4] = { 1, 0, -1 ,0 };

queue <pair<pair<int, int>, pair<int, int>>> q;

void bfs() {
	for (int i = 0; i < 4; i++) {
		q.push({ {startx, starty},{i, 0} });
	}
	visit[startx][starty] = 1;

	while (!q.empty()) {
		int x = q.front().first.first;
		int y = q.front().first.second;
		int dir = q.front().second.first;
		int cnt = q.front().second.second;
		q.pop();

		for (int k = 0; k < 4; k++) {
			int nx = x + dx[k];
			int ny = y + dy[k];
			int ncnt = cnt;

			if ((0 <= nx && nx < h) && (0 <= ny && ny < w)) {
				if (map[nx][ny] != '*') {
					if (dir != k)
						ncnt = ncnt + 1;
					if (visit[nx][ny] >= ncnt) {
						visit[nx][ny] = ncnt;							
						q.push({ { nx,ny }, { dir, ncnt } });
					}
				}
			}
		}
	}
	

}

int main() {
	scanf("%d %d", &w, &h);

	for (int i = 0; i < w; i++) {
		for (int j = 0; j < h; j++) {
			scanf("%1c", &c);
			if (c == '\n')
				j--;
			else if (c == 'C') {
				if (startx == -1) {
					startx = i;
					starty = j;
				}
				else {
					endx = i;
					endy = j;
				}
			}
			else 
				map[i][j] = c;
		}
	}

	bfs();

	printf("%d", visit[endx][endy]);


	return 0;
}
