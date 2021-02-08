#include<cstdio>

int n;

int main() {
	scanf("%d", &n);

	for(int i= 1; i < n; i++) {
		int tmp = i;
		int sum = i;
		while (tmp)
		{
			sum += tmp % 10;
			tmp /= 10;
		}
		if (sum == n) {
			printf("%d", i);
			break;
		}
	}
	printf("0");
	return 0;
}