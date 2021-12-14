#include<cstdio>
#include<algorithm>
#include<string>
#include<iostream>

using namespace std;

int l, c;
char alpha[15];

void solve(int pos, string str, int mo, int ja) {
	if (str.size() == l) {
		if (mo >= 1 && ja >= 2)
			cout << str << endl;
		return;
	}
	for (int i = pos; i < c; i++){
		if (alpha[i] == 'a' || alpha[i] == 'e' || alpha[i] == 'u' || alpha[i] == 'i' || alpha[i] == 'o')
			solve(i + 1, str + alpha[i], mo + 1, ja);
		else
			solve(i + 1, str + alpha[i], mo, ja + 1);
	}
}


int main() {

	char tmp;

	scanf("%d %d", &l, &c);
	for (int i = 0; i < c; i++) {
		scanf("%c", &tmp);
		if (tmp != ' ' && tmp != '\n')
			alpha[i] = tmp;
		else
			i--;
	}	//�̰� ��� �޴��� Ȯ���غ�����

	sort(alpha, alpha + c);

	solve(0, "", 0, 0);

	return 0;
}

/*
1. �޾Ƽ� ����
2. ó������ ���ư��� ��� ����� ���� ã�Ƽ� ���� �ɼ��ִ� ������ ����Ʈ

1�������� �������� 2���� �����ϴ� ����� ����ϴٰ� ��ͷ� �������Ѵٰ� �������ϰ� ������ ����

ã�ƺ��� dfs�� ����ؼ� ����ؼ� �̾Ƴ����� ������ �ش� �ڸ����� �Ǹ� ������ �����̶�� ����Ʈ

����� ������ �ƴϰ� dfs, ��͸� ����� ������ٸ� �ȴٸ� �׳� Ǫ�¹������ ����.

string�� �����ؼ��� c�� c++�� ȥ���ؼ� ���Ÿ� Ȱ���� �����ϵ��� ���ؾ���

** solve���� str�� %s�� �������ߴµ� string�� c++���� �����ϴ� Ŭ������ c���� ���ڿ� ����� %s�� ������ ����Ÿ����.
*/