#include<cstdio>
#include<queue>

using namespace std;

int n, m;
int map[10][10] = { 0, };
char tmp;

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

queue <int, int> q1;
queue <int, int> q2;

int main() {

	scanf("%d %d", &n, &m);
	for (int i = 0;i < n;i++) {
		for (int j = 0; j < m; j++) {
			scanf("%c", &tmp);

			if (tmp == '#')
				map[i][j] = 1;
			else if (tmp == '.')
				map[i][j] = 0;
			else if (tmp == 'B') {
				map[i][j] = 2;
				q2.push(make_pair(i, j));
			}
			else if (tmp == 'R') {
				map[i][j] = 3;
				q1.push(make_pair(i, j));
			}
			else
				map[i][j] = -1;
		}
	}


	while (!q1.empty()) {

	}

	//�������� �������� �����ִ� ���⿡ ������ �����ִ��� Ž��
	//������ ������ �Ķ������� �������ִ��� �˻�
	////�Ķ������� �������ִٸ� ����

	//������ ���������� ���డ���� �������� �������� �Ķ������� ���� �������� ����
	//���������� ������ġ�� �Ķ������� ������ġ�� ��ġ�� �ʵ��� ������ �ɾ����

	//10���̻��ߴµ��� ���θ��ϸ� �Ҽ����ٴ� ���

	return 0;
}