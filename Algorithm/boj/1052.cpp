#include<cstdio>
#include<cstring>

using namespace std;

int n, k;
int h = 1;
int bw = 0;

int main() {
	scanf("%d %d", &n, &k);

	if (k >= n) {
		printf("0");
		return 0;
	}

	else {
		while (1) {
			int temp = n;
			int cnt = 0;

			while (temp > 0) {
				if (temp % 2 == 1)
					cnt++;
				
				temp = temp / 2;
			}

			if (cnt <= k)
				break;

			bw++;
			n++;
		}
	}
	printf("%d", bw);

	return 0;
}