#include <cstdio>

int main() {
	int n,z = 0;
	char s[105];
	scanf("%d%s", &n, s);
	for (int i = 0; i < n; i++) {
		z += s[i]-'0';
	}
	printf("%d",z);
return 0;
}
