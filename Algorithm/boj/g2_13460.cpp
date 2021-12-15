#include<cstdio>
#include<queue>
#include<algorithm>

using namespace std;


struct bead {
	int rx, ry, bx, by, cnt;
};

int n, m;
char map[10][10];
int rx, ry, bx, by;
int dx[] = { 0, 0 ,1 ,-1 };
int dy[] = { 1, -1, 0, 0 };
int cnt = 0;
queue <bead> q;
bool check[10][10][10][10] = { false };



void print_map() {
	for (int i = 0;i < n;i++) {
		for (int j = 0; j < m; j++) {
			printf("%c ", map[i][j]);
		}
		printf("\n");
	}
}

void bfs() {
	while (!q.empty()) {
		int rx = q.front().rx;
		int ry = q.front().ry;
		int bx = q.front().bx;
		int by = q.front().by;
		int cnt = q.front().cnt;
		q.pop();

		if (cnt >= 10)
			break;
		if (map[rx][ry] == 'O' && map[bx][by] != 'O')
		{
			printf("%d", cnt);
			return ;
		}

		for (int i = 0; i < 4; i++) {
			int nrx = rx, nry = ry, nbx = bx, nby = by;

			while (1) {	//빨간구슬을 한방향으로 
				if (map[nrx][nry] != '#' && map[nrx][nry] != 'O') {
					nrx += dx[i]; nry += dy[i];
				}
				else {
					if (map[nrx][nry] == '#')
						nrx -= dx[i]; nry -= dy[i];
					break;
				}
			}
			while (1) {	//파란구슬을 한방향으로
				if (map[nbx][nby] != '#' && map[nbx][nby] != 'O') {
					nbx += dx[i]; nby += dy[i];
				}
				else {
					if (map[nbx][nby] == '#')
						nbx -= dx[i]; nby -= dy[i];
					break;
				}
			}

			if (nrx == nbx && nry == nby) {
				if (map[nrx][nry] != 'O') {
					int rd = abs(nrx - rx) + abs(nry - ry);
					int bd = abs(nbx - bx) + abs(nby - by);
					if (rd > bd) {
						nrx -= dx[i]; nry -= dy[i];
					}
					else {
						nbx -= dx[i]; nby -= dy[i];
					}
				}
			}

			if (check[nrx][nry][nbx][nby] == false) {
				check[nrx][nry][nbx][nby] = true;
				q.push({ nrx, nry, nbx, nby, cnt + 1 });
			}
		}
	}
	printf("-1");
}

int main() {
	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%1c", &map[i][j]);
			if (map[i][j] == '\n') {
				j--;
			}
			if (map[i][j] == 'R') {
				rx = i;
				ry = j;
			}
			else if (map[i][j] == 'B') {
				bx = i;
				by = j;
			}

		}
	}

	q.push({ rx, ry, bx, by, 0 });
	check[rx][ry][bx][by] = true;
	bfs();

	return 0;

}