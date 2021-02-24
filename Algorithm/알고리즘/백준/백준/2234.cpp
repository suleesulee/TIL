#include<cstdio>
#include<queue>

using namespace std;
int n, m;
int map[51][51];


int main() {
	scanf("%d %d", &n, &m);

	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &map[i][j]);
		}
	}
	return 0;
}
