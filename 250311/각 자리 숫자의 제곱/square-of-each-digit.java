import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);

        int n = sc.nextInt();
        System.out.println(recursesum(n));

    }

    public static int recursesum(int n){
        if (n<10){
            return n*n;
        }
        return (int) ((int) recursesum(n/10)+Math.pow(n%10,2));
    }
}