#include <stdio.h>

int main() {
    // Please write your code here.
    int n=0;
    scanf("%d\n",&n);
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}