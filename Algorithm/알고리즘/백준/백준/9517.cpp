#include<cstdio>
#include<cstring>

using namespace std;

int k, n;
int t[2][100];
int bomb = 210;
char c;
int bomb_p;
int ans = 0;
int second = 0;

int main() {
	scanf("%d", &k);
	scanf("%d", &n);
	
	bomb_p = k;

	for (int i = 0; i < n; i++) {
		scanf("%d %c", &t[0][i], &c);
		if (c == 'T') {
			t[1][i] = 1;
		}
		else if (c == 'N') {
			t[1][i] = 2;
		}
		else {
			t[1][i] = 3;
		}
		 //printf("%d %d\n", t[0][i], t[1][i]);
	}

	while (1) {
		if (t[1][ans] == 1) {
			second += t[0][ans];

			if (second > bomb) {
				break;
			}

			if (bomb_p == 8)
				bomb_p = 1;
			else
				bomb_p += 1;
		}
		else {
			second += t[0][ans];
			if (second > bomb) {
				break;
			}
		}
		ans++;
	}
	printf("%d", bomb_p);

	return 0;
}