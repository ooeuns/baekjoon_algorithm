#include <cstdio>
int main() {
    char danbi[101];
    scanf("%s", danbi);
        for (int i=0; i<100; i++) {
            printf("%c",danbi[i]);
            if (danbi[i+1]==0) {
                break;
            }
            if((i+1)%10==0) {
                printf("\n");
            }

        }
        printf("\n");
    return 0;
}
