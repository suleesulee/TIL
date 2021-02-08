#include<cstdio>
#include<queue>

using namespace std;

int n, m;
int r, c; // r -> north c -> west
int d;
int map[51][51];
int visit[51][51];
int cnt = 0;
int r_cnt = 0;

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

queue < pair<pair<int, int>, int>> q;

void go() {
	q.push(make_pair(make_pair(r, c), d));
	visit[r][c] = 1;
	cnt++;

	while (1) {
		int x = q.front().first.first;
		int y = q.front().first.second;
		int dir = q.front().second;
		q.pop();

		if (dir == 0) {
			if (0 <= y - 1 && y - 1 < m) {
				if (map[x][y - 1] == 0 && visit[x][y - 1] == 0) {
					q.push({ {x, y - 1}, 3 });
						visit[x][y - 1] = 1;
						cnt++;
					
					r_cnt = 0;
				} 
				else {
					q.push({ {x, y}, 3 });
					r_cnt++;
				}
			}
		}

		if (dir == 1) {
			if (0 <= x- 1 && x - 1 < n) {
				if (map[x-1][y] == 0 && visit[x-1][y] == 0) {
					q.push({ {x - 1, y}, 0 });
						visit[x - 1][y] = 1;
						cnt++;
					
					r_cnt = 0;
				}
				else{
					q.push({ {x, y}, 0 });
					r_cnt++;
				}
			}
		}


		if (dir == 2) {
			if (0 <= y + 1 && y + 1 < m) {
				if (map[x][y+1] == 0 && visit[x][y+1] == 0) {
					q.push({ {x, y + 1}, 1 });
						visit[x][y + 1] = 1;
						cnt++;
					
					r_cnt = 0;
				}
				else {
					q.push({ {x, y}, 1 });
					r_cnt++;
				}
			}
		}


		if (dir == 3) {
			if (0 <= x + 1 && x + 1 < n) {
				if (map[x+1][y] == 0 && visit[x + 1][y] == 0) {
					q.push({ {x + 1, y}, 2 });
						visit[x + 1][y] = 1;
						cnt++;
					
					r_cnt = 0;
				}
				else {
					q.push({ {x, y}, 2 });
					r_cnt++;
				}
			}
		}


		if (r_cnt == 4) {
			x = q.front().first.first;
			y = q.front().first.second;
			dir = q.front().second;
			q.pop();

			if (dir == 0) {
				if (map[x + 1][y] == 0) {
					q.push({ {x + 1, y}, 0 });
					if (visit[x + 1][y] == 0) {
						visit[x + 1][y] = 1;
						cnt++;
					}
					r_cnt = 0;
				}
				else if(map[x+1][y] == 1) {
					break;
				}
			}

			if (dir == 1) {
				if (map[x][y - 1] == 0) {
					q.push({ {x, y - 1}, 1 });
					if (visit[x][y - 1] == 0) {
						visit[x][y - 1] = 1;
						cnt++;
					}
					r_cnt = 0;
				}
				else if (map[x][y - 1] == 1) {
					break;
				}
			}
				
			if (dir == 2) {
				if (map[x - 1][y] == 0) {
					q.push({ {x - 1, y}, 2 });
					if (visit[x - 1][y] == 0) {
						visit[x - 1][y] = 1;
						cnt++;
					}
					r_cnt = 0;
				}
				else if (map[x - 1][y] == 1) {
					break;
				}
			}
			if (dir == 3) {
				if (map[x][y + 1] == 0) {
					q.push({ {x, y + 1}, 3 });
					if (visit[x][y + 1] == 0) {
						visit[x][y + 1] = 1;
						cnt++;
					}
					r_cnt = 0;
				}
				else if (map[x][y + 1] == 1) {
					break;
				}
			}
		}
	}
}


int main()
{
	scanf("%d %d", &n, &m);
	scanf("%d %d %d", &r, &c, &d);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &map[i][j]);
		}
	}

	go();

	printf("%d", cnt);


	//for (int i = 0; i < n; i++) {
	//	for (int j = 0; j < m; j++) {
	//		printf("%d", visit[i][j]);
	//	}
	//	printf("\n");
	//}



	return 0; 
}