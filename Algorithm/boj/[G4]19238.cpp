/*nxn 맵, m승객 
택시와 승객이 같은 위치면 최단거리0
같은 거리에 위치하면 행번호가 작은 것으로 이동
이동할때마다 연료 1씩까임
승객을 태우러 가는것도 연료까임
승객을 이동성공하면 승객태우고 움직인 거리만큼 소모한 에너지의 두배를 충전
연료가 바닥나면 실패 
도착과 동시에 0이된건 실패가 아님
*/
/*
택시를 넣고 완탐
승객의 위치 비교 만일 같은 최단거리 나오면 행이 낮은것으로 교체
택시를 승객위치로 이동 (이동가능한지 확인)
승객위치에서 택시 완탐
도착장소까지 최단거리 구하고 에너지로 이동가능하면 이동거리만큼 에너지만 추가 택시위치 변경
승객의 수 감소 시키고 이동한 승객은 삭제해버리기
도착 위치에서 다시 완탐
반복.
*/

#include<cstdio>
#include<queue>
#include<cstring>

using namespace std;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };

int n, m, fuel;
int map[21][21] = { 0 };
int c_map[21][21] = { 0 };
int taxi_x, taxi_y;
int dest_x, dest_y;
int pi_mem;
int p[400][4] = { 0 };
queue <pair<pair<int, int>, int>> q;
bool visit[21][21] = { false };
int termi = 0;

void print_map() {
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			printf("%d ", map[i][j]);
		}
		printf("\n");
	}
	printf("\n");

}

void copy_original_map() {
	memcpy(c_map, map, sizeof(map)); // c_map은 오리진맵 가짐
}

void bfs() {
	while (!q.empty()) {
		int x = q.front().first.first;
		int y = q.front().first.second;
		int cnt = q.front().second;
		q.pop();
		for (int k = 0; k < 4; k++) {
			int nx = x + dx[k];
			int ny = y + dy[k];
			if (map[nx][ny] != -1 && (0 < nx && nx <= n && 0 < ny && ny <= n)) {
				if (!visit[nx][ny]) {
					map[nx][ny] = cnt;
					visit[nx][ny] = true;
					q.push({ {nx, ny}, cnt + 1 });
				}
			}
		}
	}
}


void solve() {
	
	int tmp;
	int col = p[0][0];
	int row;
	int pi;
	int t = 3;

	while (1) {
		//1. 택시 위치에서 완탐



		print_map();


		//2. 승객 위치 비교 최단거리 승객 찾기


		for (int i = 0; i < m; i++) {
			if (p[i][0] != -1) {
				tmp = map[p[i][0]][p[i][1]];
				col = p[pi][0];
				row = p[pi][1];
				pi_mem = i;
				break;
			}
		}

		for (pi = 0; pi < m; pi++) {
			if (p[pi][0] != -1) {
				if (tmp > map[p[pi][0]][p[pi][1]]) {
					tmp = map[p[pi][0]][p[pi][1]];
					col = p[pi][0];
					row = p[pi][1];
					pi_mem = pi;
					pi = 0;
				}
				else if (tmp == map[p[pi][0]][p[pi][1]]) {
					if (col > p[pi][0]) {
						col = p[pi][0];
						row = p[pi][1];
						pi_mem = pi;
						pi = 0;
					}
				}
			}
		}


		//3. 택시를 승객에게 이동가능한지 알아보기
		if (fuel - map[col][row] >= 0) {
			fuel -= map[col][row];
		}
		else {
			printf("-1");
			return;
		}

		//4. 맵 초기화 후 현재 위치에서 완탐
		memcpy(map, c_map, sizeof(map));
		memset(visit, 0, sizeof(visit));
		q.push({ {col, row}, 1 });
		visit[col][row] = true;
		map[col][row] = 0;
		bfs();

		print_map();



		dest_x = p[pi_mem][2];
		dest_y = p[pi_mem][3];

		//printf("%d %d \n", dest_x, dest_y);

		//5. 택시 위치부터 도착장소까지 이동가능한지 알아보고 가능하면 거리 더해주고 못하면 종료
		if (fuel - map[dest_x][dest_y] >= 0)
			fuel += map[dest_x][dest_y];
		else {
			printf("-1");
			return;
		}

		//6. 현재 승객의 정보를 지우기
		for (int i = 0; i < 4; i++)
			p[pi_mem][i] = -1;

		printf("fuel: %d\n", fuel);


		//7. 도착장소에서 다시 완탐(맵초기화) * 종료조건 필요
		for (int i = 0; i < m; i++) {
			printf("p[%d][0] = %d\n", i, p[i][0]);
			if (p[i][0] == -1)
				termi++;

			if (termi == m) {
				printf("%d", fuel);
				return;
			}
			
		}
		printf("termi : %d\n", termi);
		termi = 0;


		memcpy(map, c_map, sizeof(map));
		memset(visit, 0, sizeof(visit));
		q.push({ {dest_x, dest_y}, 1 });
		visit[dest_x][dest_y] = true;
		map[dest_x][dest_y] = 0;
	}
	
}


int main() {
	scanf("%d %d %d", &n, &m, &fuel);

	for (int i = 1; i <= n;i++) {
		for (int j = 1; j <= n; j++) {
			scanf("%d", &map[i][j]);
			if (map[i][j] == 1) {
				map[i][j] = -1;
			}
		}
	}
	copy_original_map();
	
	scanf("%d %d", &taxi_x, &taxi_y);

	for (int i = 0; i < m; i++) {
		scanf("%d %d %d %d", &p[i][0], &p[i][1], &p[i][2], &p[i][3]);
	}

	q.push({{ taxi_x, taxi_y }, 1});
	visit[taxi_x][taxi_y] = true;
	map[taxi_x][taxi_y] = 0;
	bfs();
	solve();
	

	return 0;
}