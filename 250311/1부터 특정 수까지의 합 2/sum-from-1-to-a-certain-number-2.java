import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);

        int n = sc.nextInt();
        System.out.println(recursesum(n));

    }

    public static int recursesum(int n){
        if (n==1){
            return 1;
        }
        return recursesum(n-1)+n;
    }
}