// 백준 3733번 Shares
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int main()
{
	int N, S;

	while (scanf("%d %d", &N, &S) == 2)
		printf("%d\n", S / (N + 1));
	
	return 0;
}
