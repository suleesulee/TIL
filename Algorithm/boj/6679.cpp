#include<cstdio>
#include<cstring>
#include<cmath>

using namespace std;
int t1, t2, t3, t4;
int w1, w2, w3, w4;
int h1, h2, h3, h4;
int t_sum = 0, w_sum = 0, h_sum = 0;
int temp;

int main() {
	for (int i = 2992; i < 10000; i++) {
		t1 = i / 1000;
		temp = i - (1000 * t1);
		t2 = temp / 100;
		temp = temp - (100 * t2);
		t3 = temp / 10;
		t4 = temp % 10;
		t_sum = t1 + t2 + t3 + t4;

		w1 = i / pow(12, 3);
		temp = i - (pow(12, 3) * w1);
		w2 = temp / pow(12, 2);
		temp = temp - (pow(12, 2) * w2);
		w3 = temp / 12;
		w4 = temp % 12;
		w_sum = w1 + w2 + w3 + w4;

		h1 = i / pow(16, 3);
		temp = i - (pow(16, 3) * h1);
		h2 = temp / pow(16, 2);
		temp = temp - (pow(16, 2) * h2);
		h3 = temp / 16;
		h4 = temp % 16;
		h_sum = h1 + h2 + h3 + h4;

		if (t_sum == w_sum && w_sum == h_sum)
			printf("%d\n", i);
	}
	return 0;
}