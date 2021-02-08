#include<cstdio>
#include<cstring>
#include<string>

using namespace std;

int n;
int ans[1000];
int num[101][4];
int stb[101][2];
int res = 0;

void init() {
	memset(ans, 1, sizeof(ans));
	for (int i = 0; i < 123; i++) {
		ans[i] = 0;
	}
	for (int i = 988; i < 1000; i++) {
		ans[i] = 0;
	}
	for (int i = 123; i < 988; i++) {
		if ((i / 100) == (i / 10) % 10 || (i / 100) == (i % 10) % 10 || (i / 10) % 10 == (i % 10) % 10)
			ans[i] = 0;
		if (i / 100 == 0 || (i / 10) % 10 == 0 || (i % 10) % 10 == 0) {
			ans[i] = 0;
		}
	//printf("i : %d ans : %d\n", i, ans[i]);
	}
}

void solve() {
	for (int i = 123; i < 988; i++) {
		if (ans[i] != 0) {
			int h, t, o;
			h = i / 100;
			t = (i / 10) % 10;
			o = (i % 10) % 10;

			for (int j = 1; j <= n; j++) {
				int b = 0, s = 0;
				if (num[j][1] == h)
					s++;
				if (num[j][2] == t)
					s++;
				if (num[j][3] == o)
					s++;
				if (h == num[j][2] || h == num[j][3])
					b++;
				if (t == num[j][1] || t == num[j][3])
					b++;
				if (o == num[j][1] || o == num[j][2])
					b++;
				//printf("%d %d %d %d\n", s, b, stb[j][0], stb[j][1]);

				if (s == stb[j][0] && b == stb[j][1]) {
				}
				else {
					ans[i] = 0;
					break;
				}
			}
		}
		else {
			//
		}
	}

	for (int i = 123; i < 988; i++) {
		if (ans[i] != 0)
			res++;
			//printf("%d\n", i);
	}

}

int main() {
	init();
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		scanf("%d %d %d", &num[i][0], &stb[i][0], &stb[i][1]);
	}
	for (int i = 1; i <= n; i++) {
		num[i][1] = num[i][0] / 100;
		num[i][2] = (num[i][0] / 10) % 10;
		num[i][3] = (num[i][0] % 10) % 10;
		//printf("%d %d %d", num[i][1], num[i][2], num[i][3]);
	}

	solve();

	printf("%d", res);
	return 0;
}