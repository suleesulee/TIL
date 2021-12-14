#include<cstdio>
int n;
int arr[8] = { -1, };
int save[10] = { 0 , };
int cnt = 0;
int max = 0;
int main() {
	scanf("%d", &n);

	for (int i = 0; i < 7; i++) {
		if (n > 10) {
			arr[i] = n % 10;
			n /= 10;
		} else {
			arr[i] = n;
		}
	}

	for (int i = 0; arr[i] != -1; i++) {
		int k = arr[i];
		if (k == 9)
			k = 6;

		save[k]++;
	}

	//save중에 가장큰거
	//만약 6이라면 /2 해야하고 나머지 있음 +1
	max = arr[0];
	for (int i = 0; i < 10; i++) {
		if (max < save[i])
			max = save[i];
	}
	if (max == save[6]) {
		if (save[6] / 2 != 0)
			max += 1;
	}

	printf("%d", max);

	return 0;
}