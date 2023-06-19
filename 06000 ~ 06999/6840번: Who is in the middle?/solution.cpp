// 백준 6840번 Who is in the middle?
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	vector<int> arr;
	int weight;

	for (int i = 0; i < 3; i++)
	{
		cin >> weight;
		arr.push_back(weight);
	}

	sort(arr.begin(), arr.end());
	cout << arr[1] << "\n";
	
	return 0;
}
