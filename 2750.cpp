#include <cstdio>
int main() {
	int n;	// n개의 수
	int arr[1000];
	int temp;

	scanf("%d", &n);

	for (int i=0; i<n; i++) {
		scanf("%d", &arr[i]);
	}

	for (int i=0; i<n-1; i++) {
		for (int j=0; j<n-1; j++) {
			if (arr[j]>arr[j+1]) {
				temp=arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
			}
		}
	}

	for (int k=0; k<n; k++) {
		printf("%d\n", arr[k]);
	}
	return 0;
}
