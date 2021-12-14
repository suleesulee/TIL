/*nxn ��, m�°� 
�ýÿ� �°��� ���� ��ġ�� �ִܰŸ�0
���� �Ÿ��� ��ġ�ϸ� ���ȣ�� ���� ������ �̵�
�̵��Ҷ����� ���� 1������
�°��� �¿췯 ���°͵� �������
�°��� �̵������ϸ� �°��¿�� ������ �Ÿ���ŭ �Ҹ��� �������� �ι踦 ����
���ᰡ �ٴڳ��� ���� 
������ ���ÿ� 0�̵Ȱ� ���а� �ƴ�
*/
/*
�ýø� �ְ� ��Ž
�°��� ��ġ �� ���� ���� �ִܰŸ� ������ ���� ���������� ��ü
�ýø� �°���ġ�� �̵� (�̵��������� Ȯ��)
�°���ġ���� �ý� ��Ž
������ұ��� �ִܰŸ� ���ϰ� �������� �̵������ϸ� �̵��Ÿ���ŭ �������� �߰� �ý���ġ ����
�°��� �� ���� ��Ű�� �̵��� �°��� �����ع�����
���� ��ġ���� �ٽ� ��Ž
�ݺ�.
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
	memcpy(c_map, map, sizeof(map)); // c_map�� �������� ����
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
		//1. �ý� ��ġ���� ��Ž



		print_map();


		//2. �°� ��ġ �� �ִܰŸ� �°� ã��


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


		//3. �ýø� �°����� �̵��������� �˾ƺ���
		if (fuel - map[col][row] >= 0) {
			fuel -= map[col][row];
		}
		else {
			printf("-1");
			return;
		}

		//4. �� �ʱ�ȭ �� ���� ��ġ���� ��Ž
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

		//5. �ý� ��ġ���� ������ұ��� �̵��������� �˾ƺ��� �����ϸ� �Ÿ� �����ְ� ���ϸ� ����
		if (fuel - map[dest_x][dest_y] >= 0)
			fuel += map[dest_x][dest_y];
		else {
			printf("-1");
			return;
		}

		//6. ���� �°��� ������ �����
		for (int i = 0; i < 4; i++)
			p[pi_mem][i] = -1;

		printf("fuel: %d\n", fuel);


		//7. ������ҿ��� �ٽ� ��Ž(���ʱ�ȭ) * �������� �ʿ�
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