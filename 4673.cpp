#include <stdio.h>
#include <stdbool.h>

bool arr_number[10036] = { true };

void d(int n) {
	int sum = 0,a,b,c,d;
	    a = n / 1000;
        b = (n / 100) % 10;
        c = (n / 10) % 10;
        d = n % 10;
        sum = a + b + c + d + n;
	if (sum < 10036 && sum >= 1) {
		arr_number[sum] = false;
	}
}
int main() {
    for (int i=0; i<=10005; i++) arr_number[i]=true;
	int i = 1;
	while (i <= 10000) {
		d(i);
		i++;
	}

	for (i = 1; i < 10001; i++) {
		if (arr_number[i] == true) {
			printf("%d\n", i);
		}
	}
}
