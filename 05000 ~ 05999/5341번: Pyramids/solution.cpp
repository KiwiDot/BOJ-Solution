// 백준 5341번 Pyramids 
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int main()
{
	int n;

	while (true)
	{
		cin >> n;
		if (n == 0)
			break;
		cout << n * (n + 1) / 2 << "\n";
	}
	
	return 0;
}
