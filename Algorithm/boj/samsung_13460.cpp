#include<cstdio>
#include<queue>

using namespace std;

int n, m;
int map[10][10] = { 0, };
char tmp;

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

queue <int, int> q1;
queue <int, int> q2;

int main() {

	scanf("%d %d", &n, &m);
	for (int i = 0;i < n;i++) {
		for (int j = 0; j < m; j++) {
			scanf("%c", &tmp);

			if (tmp == '#')
				map[i][j] = 1;
			else if (tmp == '.')
				map[i][j] = 0;
			else if (tmp == 'B') {
				map[i][j] = 2;
				q2.push(make_pair(i, j));
			}
			else if (tmp == 'R') {
				map[i][j] = 3;
				q1.push(make_pair(i, j));
			}
			else
				map[i][j] = -1;
		}
	}


	while (!q1.empty()) {

	}

	//빨간구슬 시점에서 갈수있는 방향에 나가는 구멍있는지 탐색
	//있으면 나가고 파란구슬도 나갈수있는지 검사
	////파란구슬도 나갈수있다면 실패

	//없으면 빨간구슬이 진행가능한 방향으로 굴려보고 파란구슬도 같은 방향으로 굴림
	//빨간구슬의 현재위치와 파란구슬의 현재위치가 겹치지 않도록 조건을 걸어야함

	//10번이상했는데도 골인못하면 할수없다는 결론

	return 0;
}