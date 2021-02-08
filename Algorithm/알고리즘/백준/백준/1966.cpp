#include<cstdio>
#include<queue>
using namespace std;

int tc;
int m, n;
int tmp;
int cnt = 0;
int pop_index = -1;
queue <pair<int, int>> q;

int main()
{
	scanf("%d", &tc);
	
	while (tc--) {
		scanf("%d %d", &n, &m);

		for (int i = 0; i < n; i++) {
			scanf("%d", &tmp);
			q.push({ i, tmp });
		}

		while (1) {
			int priority = -1;
			int temp;

			for (int i = 0; i < q.size(); i++) //우선순위 높은 것 찾기
			{
				int t_index = q.front().first;
				temp = q.front().second;
				if (temp > priority) {
					priority = temp;
				}
				q.pop();
				q.push({ t_index, temp });
			}
			//printf("%d\n", priority);
			
			for (int i = 0; i < q.size(); i++) //우선순위 높은 것 빼내고 인덱스가 찾는 것 인지 보기
			{
				pop_index = q.front().first;
				int temp2 = q.front().second;
				if (priority == temp2) {	// 우선순위인 것
					q.pop();
					cnt++;
					break;
				}
				else {						//우선순위 아님
					q.pop();
					q.push({ pop_index, temp2 });
				}
			}
			//빼낸놈이 맞는놈인지 확인
			if (pop_index == m) {
				printf("%d\n", cnt);
				break;
			}
		}

		cnt = 0;
		while(!q.empty()) {
			q.pop();
		}

	}

	return 0;
}