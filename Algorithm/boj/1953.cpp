#include<cstdio>
#include<cstring>
#include<queue>
#include<vector>

using namespace std;

queue<int> q;
vector<int> v1, v2;

int visit[101];
bool map[101][101];

int n;

void solve() {

	for (int i = 1;i <= n;i++) {
		if (visit[i] != 0)
			continue;
		visit[i] = 1;
		q.push(i);

		while (!q.empty()) {
			int cur = q.front();
			q.pop();

			for (int j = 1; j <= n;j++) {
				if (visit[j] != 0)
					continue;
				
				if (map[cur][j] == false) {
					visit[j] = visit[cur] * -1;
					q.push(j);
				}
			}
		}
	}

	for (int i = 1; i <= n; i++) {
		if (visit[i] == 1)
			v1.push_back(i);
		else
			v2.push_back(i);
	}

	printf("%d\n", v1.size());
	for (int i = 0;i < v1.size();i++) {
		printf("%d ", v1[i]);
	}

	printf("\n");


	printf("%d\n", v2.size());
	for (int i = 0;i < v2.size();i++) {
		printf("%d ", v2[i]);
	}
}




int main() {
	
	memset(visit, 0, sizeof(visit));
	memset(map, true, sizeof(map));

	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		int in;
		scanf("%d", &in);
		for (int j = 0; j < in; j++) {
			int in2;
			scanf("%d", &in2);
			map[i][in2] = false;
			map[in2][i] = false;
		}
	}


	solve();

	return 0;
}