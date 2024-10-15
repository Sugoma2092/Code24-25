import java.util.Scanner;

public class ggT {
    public static void main (String[] args ){
    Scanner scan = new Scanner(System.in);
    System.out.println("Erste Variable");
    int a = scan.nextInt();
    System.out.println("Erste Variable: " + a + "  Zweite Variable");
    int b = scan.nextInt();
    System.out.println("Zweite Variable: " + b);
    scan.close();
    while (a != b && a > 1 && b > 1){
       if (a > b){
          a = a-b;  
       }
       else{
          b = b-a;
       }
       }
    if (b==1){
      a = b;
    }
    System.out.println(a);}}
