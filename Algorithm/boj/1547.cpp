#include<cstdio>
#include<cstring>

using namespace std;

int m;
int arr[51][2];
int ball = 1;

int main() {
	scanf("%d", &m);

	for (int i = 1; i <= m; i++) {
		scanf("%d %d", &arr[i][0], &arr[i][1]);
	}

	for (int i = 1; i <= m; i++) {
		if (ball == arr[i][0]) {
			ball = arr[i][1];
		}
		else if (ball == arr[i][1]) {
			ball = arr[i][0];
		}
		else {
			//nothing
		}
	}

	printf("%d", ball);

	return 0;
}