#include<cstdio>
#include <stdlib.h>


int compare(void* first, void* second)
{
	if (*(int*)first > * (int*)second)
		return 1;
	else if (*(int*)first < *(int*)second)
		return -1;
	else
		return 0;
}

int main() {
	int N;
	int arr[1000];
	int arr_size = sizeof(arr) / sizeof(int);


	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		scanf("%d", &arr[i]);
	}

	qsort(arr, arr_size, sizeof(int), compare);


	return 0;
}