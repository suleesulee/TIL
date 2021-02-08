#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

string a, b;
int res=99999999;

void minDiff(void)
{
	for (int i = 0; i <= b.length() - a.length(); i++){
		int cnt = 0;
		for (int j = 0; j < a.length(); j++) {
			if (a[j] != b[j + i])
				cnt++;
		}
		res = min(res, cnt);
	}
}


int main() {
	cin >> a >> b;
	minDiff();

	printf("%d", res);

	return 0;
}