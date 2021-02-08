#include<cstdio>
#include<queue>

using namespace std;

int tc, m, n, k;
int map[50][50] = { 0, };
int visit[50][50] = { 0, };
int in1, in2;
int cnt = 0;
queue <int, int> q;
int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

void go() {

	while (!q.empty()) {
		int x, y;
		x = q.front().first;
		y = q.front().second;
		visit[x][y] = cnt;
		q.pop();
		for (int k = 0; k < 4; k++) {
			int nx = x + dx[k];
			int ny = y + dy[k];
			if ((0 <= nx && nx < n) && (0 <= ny && ny < m) && visit[x][y] == 0) {
				q.push(nx, ny);
			}
		}
	}


}

int main() {

	scanf("%d", &tc);
	scanf("%d %d %d", &m, &n, &k);

	for (int i = 0; i < k;i++) {
		scanf("%d %d", &in1, &in2);
		map[in1][in2] = 1;
	}
	
	for (int i = 0; i < n i++) {
		for (int j = 0; j < m; j++) {
			if (map[i][j] == 1 && visit[i][j] == 0) {
				cnt++;
				q.push(i, j);
				go(i, j);
			}
		}
	}

	return 0;
}