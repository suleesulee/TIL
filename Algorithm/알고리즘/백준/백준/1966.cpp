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

			for (int i = 0; i < q.size(); i++) //�켱���� ���� �� ã��
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
			
			for (int i = 0; i < q.size(); i++) //�켱���� ���� �� ������ �ε����� ã�� �� ���� ����
			{
				pop_index = q.front().first;
				int temp2 = q.front().second;
				if (priority == temp2) {	// �켱������ ��
					q.pop();
					cnt++;
					break;
				}
				else {						//�켱���� �ƴ�
					q.pop();
					q.push({ pop_index, temp2 });
				}
			}
			//�������� �´³����� Ȯ��
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