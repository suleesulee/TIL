#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;

string input, tmp, ans;
int str_len;

void solve(int in1, int in2) {
	string a, b, c;
	a = b = c = "";

	tmp = input;

	for (int i = 0; i <= in1; i++) {
		a = a + tmp[i];
	}
	for (int i = in1 + 1; i <= in2; i++) {
		b = b + tmp[i];
	}
	for (int i = in2 + 1; i < str_len; i++) {
		c = c + tmp[i];
	}

	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());
	reverse(c.begin(), c.end());

	string tmp_ans = a + b + c;

	if (ans == "")
		ans = tmp_ans;
	else {
		if (ans > tmp_ans)
			ans = tmp_ans;
	}

}


int main() {
	ans = "";

	cin>>input;
	str_len = input.length();

	for (int i = 0; i < str_len - 1; i++) {
		for (int j = i; j < str_len - 1; j++) {
			if (i >= j) continue;
			solve(i, j);
		}
	}
	cout << ans << endl;

	return 0;
}