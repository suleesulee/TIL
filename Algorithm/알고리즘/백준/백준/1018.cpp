#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

int n, m;
char map[51][51];
char chess[8][8];
int Min = 987654321;


int ans() {
	int WB = 0;
	int BW = 0;

	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			if (((i + j) % 2 == 0 && chess[i][j] == 'W')) {
				BW++;
			}
			if (((i + j) % 2 == 1 && chess[i][j] == 'B')) {
				BW++;
			}
			if (((i + j) % 2 == 0 && chess[i][j] == 'B')) {
				WB++;
			}
			if (((i + j) % 2 == 1 && chess[i][j] == 'W')) {
				WB++;
			}
		}
	}

	return min(BW, WB);
}


void creat_map(int x, int y) {

	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			chess[i][j] = map[i + x][j + y];
		}
	}
}


int main() {

	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> map[i][j];
		}
	}


	for (int i = 0; i <= n - 8; i++) {
		for (int j = 0; j <= m - 8; j++) {
			creat_map(i, j);
			Min = min(Min, ans());
		}
	}

	printf("%d", Min);



	return 0;
}