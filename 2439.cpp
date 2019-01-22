#include <cstdio>
using namespace std;
int main() {
	int num, nnum;
	int jnum = 1;
	scanf("%d", &num);
	nnum = num;
	for (int n = 0; n < num; n++) {
		for (int i = nnum - 1; i != 0; i--) {
			printf(" ");
		}
		nnum--;
		for (int j = 0; j < jnum; j++) {
			printf("*");
		}
		jnum++;
		printf("\n");
	}
	return 0;
}
