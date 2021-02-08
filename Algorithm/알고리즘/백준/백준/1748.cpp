#include<cstdio>
#include<cstring>
#include<cmath>

using namespace std;

int n;
long long arr[10];
int cnt = 1;
long long res = 0;
long long temp;
long long temp2;

int main() {
	memset(arr, 0, sizeof(arr));
	arr[1] = 9;
	arr[9] = 9;
	for (int i = 2; i < 9; i++) {
		arr[i] = 9 * pow(10 , (i - 1)) * i;
	}

	scanf("%d", &n);

	if (n < 10) {
		printf("%d", n);
		return 0;
	}

	long long t = n;

	while (1) {
		if (t / 10 >= 10) {
			cnt++;
			t = t / 10;
		}
		else {
			cnt++;
			break;
		}
	}
	printf("cnt : %d\n", cnt);

	for (int i = 1; i < cnt; i++) {
		res += arr[i];
	}

	t = n;

	if (n == 100000000) {
		res += arr[9];
		printf("%lld", res);
		return 0;
	}
	else {

		temp = pow(10, cnt-1);

		temp2 = n - temp + 1;
		//printf("temp2 : %d\n", temp2);

		res += (temp2 * cnt);

		printf("%lld", res);
	}
	return 0;
}