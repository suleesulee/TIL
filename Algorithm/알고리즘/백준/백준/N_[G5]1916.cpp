#include<cstdio>
#include<vector>
#include<queue>

using namespace std;

const int INF = 987654321;

int n, m;
int start, end;
vector<pair<int, int> bus[1001];
int d[1001] = { INF };


void dijkstra(int start) {
	d[start] = 0; //나의 시작위치는 0
	priority_queue <pair<int, int>pq;
	pq.push(start);

	while (!pq.empty())
	{
		int cur = pq.top().second;
		int dist = -pq.top().first;
		pq.pop();

		if (d[cur] < dist)
			continue;
		for (int i = 0; i < bus[cur].size();i++) {
			int next = bus[cur][i].first;
			int next_dist = dist + bus[cur][i].second;
			if (d[next] > next_dist) {
				d[next] = next_dist;
				pq.push({ -next_dist, next });
			}
		}
	}
}


int main() {
	scanf("%d %d", &n, &m);
	for (int i = 0; i < m;i++) {
		scanf("%d %d %d", &start, &end, &cost);
		bus[start].push_back({ end, cost });
	}
	scanf("%d %d", &start, &end);

	dijkstra(start);

	retrun 0;
}