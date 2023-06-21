// 백준 7891번 Can you add this?
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int main()
{
	int t;
	long long x, y;

	cin >> t;

	while (t--)
	{
		cin >> x >> y;
		cout << x + y << "\n";
	}
	
	return 0;
}
