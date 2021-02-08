//��Ӹ������Ͽ� ���� ĭ���� �̵��ϴ� ����� ���� ���ϱ�
//���� ��ġ�� ���

#include<cstdio>
typedef struct order {
	int x;
	char c;
}order;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0 , 0 };

int sec = 0;
int n, k, l;
int apple_x, apple_y;
order info[100];
int map[101][101] = { 0 };
int snake_dir = 1; // 1: �� 2:�� 3: �� 4: ��
int snake_locate[100][2];

bool range_chk() {
	int nx = x + dx[];
	int ny = y + dy[];

	if (map[nx][ny] == 1 || (0 < nx && nx <= n) || (0 < ny && ny <= n)) {
		return false;
	}
	else
		return true;
}


void solve(){
	int snake_tail_x = 1;
	int snake_tail_y = 1;
	int map[1][1] = 1;
	snake_locate[0][0] = 1;
	snake_locate[0][1] = 1;
	bool chk;

	//������ġ�� ����, �� Ȯ��
	chk = range_chk(snake_dir);
	
	//���� �����̸� ���� �ƴϸ� ��� ����
	if (chk == false)
		printf("%d", sec);
	else {
		int nx = x + dx[];
		int ny = y + dy[];
		//������ġ�� ���?
		//������ ��� �������� �ش� ��ġ�� ������ �ٲٰ� ���� ���ο� ��ġ �߰� 
		if (map[nx][ny] == 2 )
		{	
			map[nx][ny] = 1;
		}
		else { //���� �Ӹ� ��ġ �ű�� �� ��ġ�� �ϳ� ���� ���� �ִ� ��ġ�� 0���� ���� ���� ��ġ�� �߰�
			map[nx][ny] = 1;	//��ġ�� �ű�� ���� ��ġ�� ����
			snake_tail_x;
			snake_tail_y;
		}

		//1ȸ �ð� ����
		sec++;

		//���� �������ϴ�
		for (int i = 0; i < l; i++) {
			if (sec == info[i].x) {
				if (info[i].c == 'L') {	//�������� 90
					if (snake_dir == 1) {
						snake_dir = 4;
					}
					else if (snake_dir == 2) {
						snake_dir = 1;
					}
					else if (snake_dir == 3) {
						snake_dir = 2;
					}
					else {
						snake_dir = 3;
					}
				}
				else {		//���������� 90
					if (snake_dir == 1) {
						snake_dir = 2;
					}
					else if (snake_dir == 2) {
						snake_dir = 3;
					}
					else if (snake_dir == 3) {
						snake_dir = 4;
					}
					else {
						snake_dir = 1;
					}
				}
				break;
			}
		}
	}
}


int main() {
	scanf("%d", &n);
	scanf("%d", &k);
	
	for (int i = 0; i < k; i++) {
		scanf("%d %d", &apple_x, &apple_y);
		map[apple_x][apple_y] = 2;
	}

	scanf("%d", &l);
	
	for (int i = 0; i < l; i++) 
		scanf("%d %c", &info[i].x, &info[i].c);
	
	solve();



	return 0;
}