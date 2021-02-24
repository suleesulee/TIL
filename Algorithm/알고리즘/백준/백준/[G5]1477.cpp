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
	}	//이거 어떻게 받는지 확인해봐야함

	sort(alpha, alpha + c);

	solve(0, "", 0, 0);

	return 0;
}

/*
1. 받아서 정렬
2. 처음부터 돌아가며 모든 경우의 수를 찾아서 답이 될수있는 조건을 프린트

1번까지는 구현가능 2번은 구현하는 방법에 고민하다가 재귀로 돌려야한다고 생각만하고 구현은 못함

찾아보니 dfs를 사용해서 계속해서 뽑아내도록 돌리고 해당 자리수가 되면 가능한 조건이라면 프린트

어려운 문제는 아니고 dfs, 재귀를 제대로 사용할줄만 안다면 그냥 푸는문제라고 본다.

string에 관련해서도 c와 c++을 혼용해서 쓸거면 활용이 가능하도록 잘해야함

** solve에서 str을 %s로 찍으려했는데 string은 c++에서 지원하는 클래스로 c에서 문자열 찍듯이 %s로 찍으면 못나타낸다.
*/