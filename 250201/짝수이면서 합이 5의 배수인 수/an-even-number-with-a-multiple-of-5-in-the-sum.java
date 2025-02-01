import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        goal(n);
    }
    public static void goal(int n){
        int i = n / 10;
        int num=n%10;
        if(n%2==0 && ((n%10)+i)%5==0){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}