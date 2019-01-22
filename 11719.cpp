#include <iostream>
#include <string>

using namespace std;

int main()
{
	string str;
	string ans;

	for (int i = 0; i < 100 && !cin.eof(); i++)
	{
		getline(cin, str);
		if(i>0)
			ans += "\n";
		ans = ans + str;
	}

	cout << ans;

	return 0;
}
