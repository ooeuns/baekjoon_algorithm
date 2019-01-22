#include <cstdio>
using namespace std;
int main() {
	int num, nnum;
	int jnum = 0;
	scanf("%d", &num);
	nnum = num;
	for (int n = 0; n < num; n++) {
		for (int j = 0; j < jnum; j++) {
			printf(" ");
		}
		jnum++;

		for (int i = nnum; i != 0; i--) {
			printf("*");
		}

		nnum--;
		printf("\n");
	}
	return 0;
}
