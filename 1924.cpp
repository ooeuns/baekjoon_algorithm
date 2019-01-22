#include <cstdio>
using namespace std;
int main() {
	int month[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	int mon, day, num;
	int n;
	scanf("%d %d", &mon, &day);
	num = day;
	for (int i = 0; i < mon -1; i++) {
		num += month[i];
	}
	n = num % 7;
	switch (n) {
	case 1:
		printf("MON");
		break;
	case 2:
		printf("TUE");
		break;
	case 3:
		printf("WED");
		break;
	case 4:
		printf("THU");
		break;
	case 5:
		printf("FRI");
		break;
	case 6:
		printf("SAT");
		break;
	case 0:
		printf("SUN");
		break;
	}
	return 0;
}
