#include<cstdio>

using namespace std;

int l, n;
int p, k;
int cake[1001];
int max_cake = 0;
int max_pre = 0;
int cnt = 0;
int real_max = 0;
int real_man = 0;

int main() {
	int temp;

	scanf("%d", &l);
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		scanf("%d %d", &p, &k);

		if (max_cake == 0) {
			max_cake = k - p + 1;
			max_pre = i;
		}
		else {
			if (max_cake < k - p + 1) {
				max_cake = k - p + 1;
				max_pre = i;
			}
		}

		for (int j = p; j <= k; j++) {
			if (cake[j] == 0) {
				cake[j] = i;
				cnt++;
			}
		}
		if (real_man == 0) {
			real_max = cnt;
			real_man = i;
		}
		else {
			if (cnt > real_max) {
				real_max = cnt;
				real_man = i;
			}
		}
		cnt = 0;
	}

	printf("%d\n%d", max_pre, real_man);

	return 0;
}