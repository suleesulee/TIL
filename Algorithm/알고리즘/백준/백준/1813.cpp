#include<cstdio>
#include<cstring>

using namespace std;
int n;
int in;
int arr[100001];

int main() {
	memset(arr, 0, sizeof(arr));
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &in);
		arr[in]++;
	}
	for (int i = 100000; i >= 0; i--) {
		if (arr[i] == i) {
			printf("%d", i);
			return 0;
		}
	}
	printf("-1");

	return 0;
}