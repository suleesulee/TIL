#include<cstdio>
#include<cmath>

int main() {
	int n, r, c;
	int len;
	int x, y;
	int ans = 0;

	scanf("%d %d %d", &n, &r, &c);

	len = pow(2, n);
	
	x = len / 2;
	y = x;

	/*
	  1   |   2
	      |
	-------------
	  3   |   4
		  |
	*/

	while (n-- > 0) {
		int tmp = pow(2, n) / 2;
		int skip = pow(4, n);
		
		if (r < y && c < x) {
			x -= tmp;
			y -= tmp;
		}
		else if (r < y && x <= c) {
			x += tmp;
			y -= tmp;
			ans += skip;// �� ��и��� ��ŵ�� ��
		}
		else if (r >= y && c < x) {
			x -= tmp;
			y += tmp;
			ans += skip * 2;
		}
		else {
			x += tmp;
			y += tmp;
			ans += skip * 3;
		}
	}

	printf("%d", ans);
	return 0;
}

/*���������� ���� Ǯ�̸� ����ߴ�.
��ŵ�� �ϸ� �������ϴ°��� ���� ���� Ǯ�̰����� ����.
�ٸ� ����κп��� r,c�� �����ϴ� ���� ã�Ƽ� ���ƾ��ϴ��� ��Ŵ�
x,y ���� ����ؾ��Ѵٴ°��� �˾Ҵ�.
n������ ����� �ѵ� �ʿ���� �и��� ��ŵ���� ���ϰ� tmp ���� x,y ���� �и��� �»���� ���� �־�
����ؼ� ��������� ������ ������ 4ĭ���� r,c�� ã�°����� �ݺ���
�ش� r,c�� ���� �湮�ϴ��� ���´�.

*/