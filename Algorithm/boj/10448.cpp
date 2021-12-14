#include<cstdio>
#include<cstring>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
int tc;
int t[100];
int in;
int temp;

void make_t() {
	memset(t, 0, sizeof(t));
	for (int i = 1; i < sizeof(t); i++) {
		t[i] = i * (i + 1) / 2;
		if (t[i] > 1000) {
			t[i] = 0;
			temp = i - 1;
			break;
		}
	}
}


int check_t(int a) {

	for (int i = 1; i <= temp; i++) {
		for (int j = 1; j <= temp; j++) {
			for (int k = 1; k <= temp; k++) {
				if (t[i] + t[j] + t[k] == a)
					return 1;
			}
		}
	}
	return 0;
}


int main() {
	make_t();

	scanf("%d", &tc);

	for (int i = 0; i < tc; tc--) {
		scanf("%d", &in);

		printf("%d\n", check_t(in));
	}

	return 0;
}