#include <cstdio>

int number;
int k;
int arr[10];

int calculator(int *arr, int n, int k) {
   int count = 0;
   if (k != 0) {
      for (int i = n; i >= 0; i--) {
         while (k - arr[i] >= 0) {
            k = k - arr[i];
            count++;

            if(k==0) {
            return count;
            //  break;
            }
         }
      }
   }
   return count;
}

int main(void) {
   scanf("%d %d", &number, &k);
   for (int i = 0; i < number; i++) {
      scanf("%d", &arr[i]);
   }

   printf("%d", calculator(arr, number - 1, k));
   return 0;
}