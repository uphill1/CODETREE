#include <stdio.h>

int main() {
    // Please write your code here.
    int n,m;
    scanf("%d %d\n",&n,&m);
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}