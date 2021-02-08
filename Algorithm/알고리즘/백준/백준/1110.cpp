#include<cstdio>

int n;
int save;
int sum;
int cnt = 0;
int main()
{
	scanf("%d", &n);

	save = n;

	while (1) {
		if(n < 10){
			n = n * 11;
			cnt++;
		}
		else {
			sum = (n / 10) + (n % 10);

			if (sum > 10)
				sum = 1;

			n = (n % 10) * 10 + sum;
			cnt++;

		}
		if (save == n)
			break;
	}

	printf("%d", cnt);

	return 0;
}