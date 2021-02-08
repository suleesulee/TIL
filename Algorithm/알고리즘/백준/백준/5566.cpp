#include<cstdio>
#include<cstring>

#define MAX 1002
using namespace std;

int n, m;
int map[MAX];
int dice[MAX];
int state = 1;

int main() {

	map[1] = 0;
	scanf("%d %d", &n, &m);
	for (int i = 1; i <= n ; i++) {
		scanf("%d", &map[i]);
	}

	for (int i = 0; i < m; i++) {
		scanf("%d", &dice[i]);
	}

	int dice_cnt = 0;
	
	while (state < n ) {
		state += dice[dice_cnt];
		state += map[state];
		dice_cnt++;
	}

	printf("%d", dice_cnt);

	return 0;
}
