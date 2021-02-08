#include<cstdio>
#include<cstring>

using namespace std;

int l_max = 5000;
int w_max = 4000;
int r, b;
int l, w;
int total;

int main() {
	scanf("%d %d", &r, &b);
	for (int i = 1; i <= l_max; i++) {
		for (int j = 1; j <= w_max; j++) {
			if (r + b == i * j) {
				if (r == (i * 2) + (j - 2) * 2) {
					l = i;
					w = j;
					break;
				}
				else if (r == j * 2 + (i - 2) * 2) {
					l = j;
					w = i;
					break;
				}
			}
		}
	}

	printf("%d %d", l, w);
	return 0;
}
