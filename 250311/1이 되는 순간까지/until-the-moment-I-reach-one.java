import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println(untill1(sc.nextInt()));


    }

    public static int untill1(int n){
        //종료조건
        if(n==1){
            return 0;
        }

        if(n%2==0){
            n/=2;
        }else{
            n/=3;
        }
        return untill1(n)+1;
    }
}