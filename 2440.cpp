#include <cstdio>
using namespace std;
int main() {
	int num, jnum;
	scanf("%d", &num);
	jnum = num;
	for (int j = 0; j < num; j++) {
		for (int i = jnum; i != 0; i--) {
			printf("*");
		}
		jnum--;
		printf("\n");
	}
	return 0;
}
