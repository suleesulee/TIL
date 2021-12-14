#include<cstdio>
#include<cstring>
#include<queue>
#include<vector>
using namespace std;

queue<int> q;	//현재 위치 확인용
vector<int> v;	//뽑아내야하는 순서
int min = 9999999;

int n, m;
int temp;
int cur = 1;
int next_l;
int cnt = 0;

void find_d(int in) {
	int tmp1, tmp2;

	if (cur - v[in] > 0)
		tmp1 = cur - v[in];
	else
		tmp1 = v[in] - cur;

	if(cur < v[in])
		tmp2 = n + cur - v[in];
	else
		tmp2 = n - cur + v[in];

	printf("tmp1 : %d tmp2 : %d\n", tmp1, tmp2);
	
	if (cur - v[in] == 0) {
		cur += 1;
		return;
	}
	else {
		cur = v[in];
	}
	
	if (tmp1 > tmp2) {
		cnt += tmp2;
		printf("cur : %d\n", cur);
		printf("tmp2 : %d\n", tmp2);
		printf("v[in] : %d\n", v[in]);
	}

	else {
			cnt += tmp1;

		printf("cur : %d\n", cur);
		printf("tmp1 : %d\n", tmp1);
		printf("v[in] : %d\n", v[in]);
	}

}


int main() {
	scanf("%d %d", &n, &m);

	for (int i = 0; i < m; i++) {
		scanf("%d", &temp);
		v.push_back(temp);
	}

	for (int i = 0; i < m; i++) {
		find_d(i);
	}

	printf("%d", cnt);
}