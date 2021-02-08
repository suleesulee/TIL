#include<cstdio>
#include<cstring>

using namespace std;

int n, k;
int arr[20];
int n_arr[20];

int main() {
	scanf("%d %d", &n, &k);

	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
		getchar();
	}
	for (int i = 0;  i < k; i++) {
		for (int j = 0; j < n - i; j++) {
			arr[j] = arr[j + 1] - arr[j];
		}
	}

	for (int i = 0; i < n - k -1 ; i++) {
		printf("%d,", arr[i]);
	}
	printf("%d", arr[n - k - 1]);
	

	return 0;
}