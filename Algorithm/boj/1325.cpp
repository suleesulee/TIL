#include<cstdio>
#include<vector>
#include<queue>

using namespace std;

int n, m;
vector<int> v[10001];
queue<int> q;
int ans[10001];
int Max = 0;
int max_cnt = 0;

int main() {

	scanf("%d %d", &n, &m);

	for (int i = 0; i < m; i++) {
		int s, e;
		scanf("%d %d", &e, &s);
		v[s].push_back(e);
	}


	for (int i = 1; i <= n; i++) {
		int cnt = 0;
		int visit[10001] = {};

		q.push(i);
		visit[i] = 1;
		cnt++;

		while (!q.empty()) {
			int now = q.front();
			q.pop();

			for (int j = 0; j < v[now].size(); j++) {
				int tmp = v[now][j];
				if (visit[tmp] == 0) {
					q.push(tmp);
					visit[tmp] = 1;
					cnt++;
				}
			}
		}

		if (cnt > Max) {
			max_cnt = 0;
			Max = cnt;
			ans[max_cnt++] = i;
		}
		else if (cnt == Max) {
			ans[max_cnt++] = i;
		}
	}

	for (int i = 0; i < max_cnt; i++) {
		printf("%d ", ans[i]);
	}
	return 0;
}
