#include<iostream>
using namespace std;

int main(void) {
    int num=0;
    scanf("%d", &num);
    if(num>=1 && num<=100) {
        // top-picture
        int write = 1;
        int total = num*2;

        for(int k=0; k<num; k++) {
            for(int i=0; i<write; i++) {    // *
                printf("*");
            }
            int blank = total - write*2;
            for(int i=0; i<blank; i++) {    // " "
                printf(" ");
            }
            for(int i=0; i<write; i++) {    // *
                printf("*");
            }
            printf("\n");
            write++;
        }
        
        //botton-picture
        num--;
        write-=2;

        for(int k=0; k<num; k++) {
            for(int i=0; i<write; i++) {    // *
                printf("*");
            }
            int blank = total - write*2;
            for(int i=0; i<blank; i++) {    // " "
                printf(" ");
            }
            for(int i=0; i<write; i++) {    // *
                printf("*");
            }
            printf("\n");
            write--;
        }

    }
    return 0;
}