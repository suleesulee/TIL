#include<cstdio>
#include<cstring>

using namespace std;

int a, b, c;
int in1, in2;
int one[101];
int two[101];
int three[101];
int one_cnt= 0;
int two_cnt = 0;
int three_cnt = 0;
int res;

int main() {
	scanf("%d %d %d", &a, &b, &c);

	for (int i = 0; i < 3; i++) {
		scanf("%d %d", &in1, &in2);

		if (i == 0) {
			for (int j = in1; j < in2; j++) {
				one[j] = 1;
			}
		}
		else if (i == 1) {
			for (int j = in1; j < in2; j++) {
				two[j] = 1;
			}
		}
		else {
			for (int j = in1; j < in2; j++) {
				three[j] = 1;
			}
		}
	}

	for (int i = 1; i <= 100; i++) {
		if (one[i] == 1) {
			if (two[i] == 1) {
				if (three[i] == 1) {
					//세대 모두
					three_cnt++;
				}
				else {
					//1,2 두대만
					two_cnt++;
				}
			}
			else {
				if (three[i] == 1) {
					//1,3 두대만
					two_cnt++;
				}
				else {
					//1번차만
					one_cnt++;
				}
			}
		}
		else {
			if (two[i] == 1) {
				if (three[i] == 1) {
					//2,3 두대만
					two_cnt++;
				}
				else {
					//2 한대만
					one_cnt++;
				}
			}
			else {
				if (three[i] == 1) {
					//3 한대만
					one_cnt++;
				}
				else {
					//한대도 없음
				}
			}
		}
	}
	res = (a * one_cnt) + (2 * b * two_cnt) + (3 * c * three_cnt);

	printf("%d", res);

	return 0;
}