import java.util.Scanner;

//TIP 코드를 <b>실행</b>하려면 <shortcut actionId="Run"/>을(를) 누르거나
// 에디터 여백에 있는 <icon src="AllIcons.Actions.Execute"/> 아이콘을 클릭하세요.
public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(oddeven(n));

    }
    public static int oddeven(int n){
        if(n==2){
            return 2;
        }
        if(n==1){
            return 1;
        }

        if(n%2==0){
            return oddeven(n-2)+n;
        }else{
            return oddeven(n-2)+n;
        }

    }
}