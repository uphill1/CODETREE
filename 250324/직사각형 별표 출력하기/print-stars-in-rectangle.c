#include <stdio.h>

int main() {
    // Please write your code here.
    int n,m;
    scanf("%d %d\n",&n,&m);
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}