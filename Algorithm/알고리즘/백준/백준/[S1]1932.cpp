#include<cstdio>
#include<algorithm>

using namespace std;

int main() {
	int n;
	int tri[501][501];
	int d[501][501];

	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			scanf("%d", &tri[i][j]);
		}
	}
	
	d[1][1] = tri[1][1];

	for (int i = 2; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			if (j == 1) {
				d[i][1] = d[i - 1][1] + tri[i][1];
			}
			else if (j == i) {
				d[i][j] = d[i - 1][j - 1] + tri[i][j];
			}
			else {
				d[i][j] = max(d[i - 1][j - 1] + tri[i][j], d[i - 1][j] + tri[i][j]);
			}
		}
	}

	int max = d[n][1];
	for (int i = 1; i <= n; i++) {
		if (max < d[n][i]) {
			max = d[n][i];
		}
	}

	printf("%d", max);

	return 0;
}
/* 다이나믹프로그래밍 문제
그냥 풀었다 .. 점화식 세우고 그냥 풀면 되는 문제였음
첫번째와 마지막번째에 들어갈 값만 그냥 더하면 되었고 중간에 끼인 삼각형들은 위에서 더할수있는 값중에 큰 값이 되는걸 선택하면되었다.*/