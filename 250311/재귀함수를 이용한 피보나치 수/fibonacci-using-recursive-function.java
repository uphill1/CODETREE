import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(pibo(n));
    }

    public static int pibo(int n){
        if(n==1){
            return 1;
        }
        if(n==2){
            return 1;
        }


        return pibo(n-1)+pibo(n-2);
    }


}