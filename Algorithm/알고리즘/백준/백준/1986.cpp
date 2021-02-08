#include<cstdio>
#include<cstring>

void check();
void check_queen(int x, int y);
void check_knight(int x, int y);
void print_map();
using namespace std;

int n, m;
int x, y;
int Queen, Knight, Pawn;
int map[1001][1001];


//안전함 0 안전하지 않음 1 퀸 2 나이트3 폰4

void check() {
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (map[i][j] == 2) {
				check_queen(i, j);
			}
		}
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (map[i][j] == 3) {
				check_knight(i, j);
			}
		}
	}
}

void check_queen(int x, int y) {
	//가로 (+1, 0), (-1 0)
	for (int i = x + 1; i <= n; i++) {
		if (map[i][y] != 3 || map[i][y] != 4 || map[i][y] != 2)
			map[i][y] = 1;
		else
			break;
	}
	for (int i = x - 1; i > 0; i--) {
		if (map[i][y] != 3 || map[i][y] != 4 || map[i][y] != 2)
			map[i][y] = 1;
		else
			break;
	}
	//세로 (0, +1), (0, -1)
	for (int i = y + 1; i <= m; i++) {
		if (map[x][i] != 3 || map[x][i] != 4 || map[x][i] != 2)
			map[x][i] = 1;
		else
			break;
	}
	for (int i = y - 1; i > 0; i--) {
		if (map[x][i] != 3 || map[x][i] != 4 || map[x][i] != 2)
			map[x][i] = 1;
		else
			break;
	}

	//대각(+1, +1), (+1, -1), (-1, -1), (-1, +1)
	for (int i = x + 1, j = y + 1; i <= n && j <= m; i++, j++) {
		if (map[i][j] != 3 || map[i][j] != 4 || map[i][j] != 2)
			map[i][j] = 1;
		else
			break;
	}
	for (int i = x+1, j = y-1; i <= n && j > 0; i++, j--) {
		if (map[i][j] != 3 || map[i][j] != 4 || map[i][j] != 2)
			map[i][j] = 1;
		else
			break;
	}
	for (int i = x-1, j = y+1; i > 0 && j <= m; i--, j++) {
		if (map[i][j] != 3 || map[i][j] != 4 || map[i][j] != 2)
			map[i][j] = 1;
		else
			break;
	}
	for (int i = x-1, j = y-1; i > 0 && j > 0; i--, j--) {
		if (map[i][j] != 3 || map[i][j] != 4 || map[i][j] != 2)
			map[i][j] = 1;
		else
			break;
	}
}

void check_knight(int x, int y) {
	if (0 < x-2 && x-2 <= n && 0 < y+1 && y+1 <= m) {
		if(map[x-2][y+1] == 0)
			map[x - 2][y + 1] = 1;
	}
	if (0 < x - 1 && x -1 <=n && 0<y+2 && y + 2 <=m) {
		if (map[x - 1][y + 2] == 0)
			map[x - 1][y + 2] = 1;
	}
	if (0<x+1 && x + 1<=n && 0 < y+2 && y + 2 <= m) {
		if (map[x + 1][y + 2] == 0)
			map[x + 1][y + 2] = 1;
	}
	if (0<x+2 && x + 2 <= n && 0 < y +1 && y + 1 <= m) {
		if (map[x + 2][y + 1] == 0)
			map[x + 2][y + 1] = 1;
	}
	if ( 0 < x+2 && x + 2 <= n && 0 < y -1 && y-1 <= m) {
		if (map[x + 2][y - 1] == 0)
			map[x + 2][y - 1] = 1;
	}
	if ( 0<x+1 && x + 1 <=n && 0 < y - 2 && y-2 <=m) {
		if (map[x + 1][y - 2] == 0)
			map[x + 1][y - 2] = 1;
	}
	if (0 < x - 1 && x-1<=n && 0 < y - 2 && y-2 <=m) {
		if (map[x - 1][y - 2] == 0)
			map[x - 1][y - 2] = 1;
	}
	if (0 < x - 2 && x -2 <=n && 0 < y - 1 && y-1 <=m) {
		if (map[x - 2][y - 1] == 0)
			map[x - 2][y - 1] = 1;
	}
}

int check_safe() {
	int cnt = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (map[i][j] == 0) {
				cnt++;
			}
		}
	}
	return cnt;
}


void print_map() {
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			printf("%d ", map[i][j]);
		}
		printf("\n");
	}
}

int main() {
	memset(map, 0, sizeof(map));

	scanf("%d %d", &n, &m);
	
	
	scanf("%d", &Queen);
	for (int i = 0; i < Queen; i++) {
		scanf("%d %d", &x, &y);
		map[x][y] = 2;
	}
	scanf("%d", &Knight);
	for (int i = 0; i < Knight; i++) {
		scanf("%d %d", &x, &y);
		map[x][y] = 3;
	}
	scanf("%d", &Pawn);
	for (int i = 0; i < Pawn; i++) {
		scanf("%d %d", &x, &y);
		map[x][y] = 4;
	}
	check();
	//print_map();
	printf("%d", check_safe());

	return 0;
}