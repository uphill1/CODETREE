import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] count = new int[10];
        while(true){
            int n = sc.nextInt();
            if(n==0){
                break;
            }
            int temp = n/10;
            count[temp]++;
        }
        for(int i =1 ;i<10 ;i++){
            System.out.println(i+" - "+count[i]);
        }
    }
}