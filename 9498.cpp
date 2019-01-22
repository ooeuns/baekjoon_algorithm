#include <cstdio>
int main() {
    int danbi;
    scanf("%d", &danbi);
    if(danbi<=100 && danbi>=90) {
        printf("A");
    }
    else if(danbi<=89 && danbi >= 80) {
        printf("B");
    }
    else if(danbi<=79 && danbi >= 70) {
        printf("C");
    }
    else if(danbi<=69 && danbi >= 60) {
        printf("D");
    }
    else {
        printf("F");
    }
    return 0;
}
