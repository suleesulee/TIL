#include<cstdio>

int n;
int ans = 1;

int main() {
	scanf("%d", &n);

	if (n == 0) {
		printf("0");
		return 0;
	}

	for (int i = 1; i <= n; i++) {
		ans *= i;
	}

	printf("%d", ans);

	return 0;
}