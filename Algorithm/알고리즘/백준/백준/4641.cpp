#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>

using namespace std;

vector <int> v;
int in;

void solve() {
	int cnt = 0;
	sort(v.begin(), v.end());

	for (int i = 0; i < v.size(); i++) {
		for (int j = 0; j < v.size(); j++) {
			if (v[i] == v[j] * 2) {
				cnt++;
				break;
			}
		}
	}
	printf("%d\n", cnt);
}

int main() {
	while (1)
	{
		scanf("%d", &in);
		if (in == 0) {
			solve();
			v.clear();
		}
		else {
			v.push_back(in);
		}

		if (in == -1) {
			break;
		}
	}

}