#include<cstdio>

int n;
int arr[100];
int prime[5] = { 2,3,5,7,11 };
int cnt = 0;

int main() {
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	for (int i = 0; i < n;i++) {
		if (arr[i] == 1)
			continue;

		for(int j = 0; j < 5; j++){
			if (arr[i] == prime[j])
				continue;
			
			if (arr[i] % prime[j] != 0)
				cnt++;
		}
	}

	printf("%d", cnt);

	return 0;
}