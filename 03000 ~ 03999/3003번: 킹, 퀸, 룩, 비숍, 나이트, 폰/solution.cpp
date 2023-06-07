// 백준 3003번 킹, 퀸, 룩, 비숍, 나이트, 폰
#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	int a, b, c, d, e, f;
	cin >> a >> b >> c >> d >> e >> f;

	printf("%d %d %d %d %d %d", 1-a, 1-b, 2-c, 2-d, 2-e, 8-f);
	
	return 0;
}
