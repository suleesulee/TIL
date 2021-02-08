#include<cstdio>
int n, m;
int arr[100];
int sum = 0;
int ans = 0;
int main() {
	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				if (i != j && j != k && k != i) {
					sum = arr[i] + arr[j] + arr[k];
					if (m >= sum && ans < sum) {
						ans = sum;
					}
				}
			}
		}
	}

	printf("%d", ans);
	return 0;
}