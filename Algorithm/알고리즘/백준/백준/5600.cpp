#include<cstdio>

using namespace std;

int a, b, c;
int n;
int i[1001], j[1001], k[1001], r[1001];
int ans[301];
int main() {
	

	for (int l = 1; l < 301; l++) {
		ans[l] = 2;
	}
	scanf("%d %d %d", &a, &b, &c);

	scanf("%d", &n);

	for (int l = 1; l <= n; l++) {
		scanf("%d %d %d %d", &i[l], &j[l], &k[l], &r[l]);
	}

	for (int l = 1; l <= n; l++) {
		if (r[l] == 1) {
			ans[i[l]] = 1;
			ans[j[l]] = 1;
			ans[k[l]] = 1;
		}
	}

	for (int l = 1; l <= n; l++) {
		if (r[l] == 0) {
			if (ans[i[l]] == 1 && ans[j[l]] == 1 && ans[k[l]] == 2) {
				ans[k[l]] = 0;
			}
			if (ans[i[l]] == 1 && ans[k[l]] == 1 && ans[j[l]] == 2) {
				ans[j[l]] = 0;
			}
			if (ans[j[l]] == 1 && ans[k[l]] == 1 && ans[i[l]] == 2) {
				ans[i[l]] = 0;
			}
		}
	}

	for (int l = 1; l <= a+b+c; l++) {
		printf("%d\n", ans[l]);
	}
	return 0;
}