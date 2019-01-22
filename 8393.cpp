#include <cstdio>
using namespace std;
int main() {
	int n;
	int num=0;
	scanf("%d", &n);
	for (int i = 1; i < n+1; i++) {
		num +=i;
	}
	printf("%d", num);
	return 0;
}
