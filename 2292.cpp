#include <stdio.h>

int main(void){
	long long unsigned int n;
	long long unsigned int m;
	scanf("%llu", &n);
	// 초기 조건을 만족하기 위해 +4
	n += 4;
	n /= 6;
	for(long long unsigned int i = 0;i < 100000000;i++){
		m = i*(i+1)/2;
		if(n <= m){
            // 처음을 포함하기 때문에 +1
			printf("%llu", i+1);
			break;
		}
	}
	return 0;
}
