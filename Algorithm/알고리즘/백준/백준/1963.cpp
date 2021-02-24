#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <queue>

using namespace std;

int tc;
int in, out;
bool prime[10001];
int visit[10001] = { 0, };
int check = 0;
int digit[4];
int ch_num;

void change_digit(int in) {
	//천의자리부터
	digit[0] = in / 1000;
	digit[1] = (in / 100) % 10;
	digit[2] = (in / 10) % 10;
	digit[3] = in % 10;
	//printf("%d %d %d %d ", digit[0], digit[1], digit[2], digit[3]);
}

int change_prime(int in, int i, int c_num) {
	int temp = in;

	change_digit(temp);

	if (i == 0) {
		if (c_num == 0)
			return -1;
		else
			digit[0] = c_num;
	}
	else if (i == 1) {
		digit[1] = c_num;
	}
	else if (i == 2) {
		digit[2] = c_num;
	}
	else if (i == 3) {
		digit[3] = c_num;
	}

	temp = digit[0] * 1000 + digit[1] * 100 + digit[2] * 10 + digit[3];

	if (prime[temp] == 1 && temp != in) {
		return temp;
	}
	else
		return -1;
}


void eratosnes() {
	prime[0] = 0;
	prime[1] = 0;
	for (int i = 2; i * i < 10000; i++) {
		for (int j = i * i; j < 10000; j += i) {
			prime[j] = 0;
		}
	}
}

void bfs(int in) {
	queue <pair<int, int>> q;
	q.push({ in, 0 });
	visit[in] = 1;

	while (!q.empty()) {
		int Nin = q.front().first;
		int cnt = q.front().second;
		q.pop();

		if (Nin == out) {
			printf("%d\n", cnt);
			check = 1;
			break;
		}

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 10; j++) {
				ch_num = change_prime(Nin, i, j);
				if (ch_num != -1 && visit[ch_num] == 0) {
					visit[ch_num] = 1;
					q.push({ ch_num, cnt + 1 });
				}
			}
		}
	}

}


int main() {
	memset(prime, true, sizeof(prime));
	eratosnes();

	scanf("%d", &tc);
	for (int i = 0; i < tc; i++) {
		scanf("%d %d", &in, &out);
		bfs(in);

		if (check == 0) {
			printf("Impossible\n");
		}

		memset(visit, 0, sizeof(visit));
	}

	return 0;
}