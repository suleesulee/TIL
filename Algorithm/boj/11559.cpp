#include<cstdio>
#include<queue>
#include<vector>
#include<cstring>

using namespace std;

char map[13][7];
int visit[13][7];

queue<pair<int, int>> q;
queue<pair<int, int>> save_q;
vector <pair<int, int>> v[18];
int v_cnt = 0;

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

int d_cnt = 0;
int tmp1 = -1;
int tmp2 = -1;
int down = 0;

int t_puyo = 0;
int puyo = 0;

char ch;

void bfs() {
	int cnt = 1;
	while (!q.empty())
	{
		int x = q.front().first;
		int y = q.front().second;
		char c = map[x][y];
		q.pop();

		for (int k = 0; k < 4; k++) {
			int nx = dx[k] + x;
			int ny = dy[k] + y;
			if (0 <= nx && nx < 12 && 0 <= ny && ny < 6) {
				if (map[nx][ny] == c && visit[nx][ny] == 0) {
					q.push({ nx, ny });
					visit[nx][ny] = 1;
					v[v_cnt].push_back({ nx, ny });
					cnt++;
				}
			}
		}
	}

	if (cnt >= 4) {
		puyo++;
		v_cnt++;
	}
	else {
		v[v_cnt].clear();
	}
}

int main()
{
	for (int i = 0; i < 12; i++) {
		for (int j = 0; j < 6; j++) {
			scanf("%1c", &ch);
			if (ch != '\n')
				map[i][j] = ch;
			else
				j--;
		}
	}


	// for (int i = 0; i < 12; i++) {
	// 	for (int j = 0; j < 6; j++) {
	// 		printf("%c", map[i][j]);
	// 	}
	// 	printf("\n");
	// }


	while (1) {
		//for(int a = 0; a < 3; a++) {
		for (int i = 0; i < 12; i++) {
			for (int j = 0; j < 6; j++) {
				if (visit[i][j] == 0 && map[i][j] != '.') {
					q.push({ i, j });
					visit[i][j] = 1;
					v[v_cnt].push_back({ i, j });
					bfs();
				}
			}
		}

		//printf("%d", v_cnt);


		// ¸Ê º¯°æ
		for (int i = 0; i < v_cnt; i++) {
			for (int j = 0; j < v[i].size(); j++) {
				int x = v[i][j].first;
				int y = v[i][j].second;
				map[x][y] = '.';
			}
		}


		///////////////////////
		// printf("\n");
		// printf("\n");
		// for (int i = 0; i < 12; i++) {
		// 	for (int j = 0; j < 6; j++) {
		// 		printf("%c", map[i][j]);
		// 	}
		// 	printf("\n");
		// }
		/////////////////////

		for (int j = 0; j < 6; j++) {
			for (int i = 11; i >= 0; i--) {
				if (map[i][j] == '.') {
					d_cnt++;
					if (tmp1 == -1) {
						tmp1 = i;
					}
				}

				if (d_cnt != 0) {
					if (map[i][j] != '.') {
						tmp2 = i;
					}
				}

				if (tmp1 != -1 && tmp2 != -1) {
					down = tmp1 - tmp2;
					for (int k = tmp1; k >= down; k--) {
						map[k][j] = map[k - down][j];
					}
					for (int l = 0; l < down; l++) {
						map[l][j] = '.';
					}

					i = 11;
					tmp1 = -1;
					tmp2 = -1;
					d_cnt = 0;
				}
				else if (tmp2 == -1 && tmp1 != -1 && i == 0) {
					tmp1 = -1;
					tmp2 = -1;
					d_cnt = 0;
				}
			}
		}

		// printf("\n");
		// printf("\n");
		// for (int i = 0; i < 12; i++) {
		// 	for (int j = 0; j < 6; j++) {
		// 		printf("%c", map[i][j]);
		// 	}
		// 	printf("\n");
		// }

		//Å»ÃâÁ¶°Ç
		if (t_puyo == puyo)
			break;

		//ºñÁþ ÃÊ±âÈ­
		memset(visit, 0, sizeof(visit));

		t_puyo = puyo;
	}

	printf("%d", puyo);


	return 0;
}