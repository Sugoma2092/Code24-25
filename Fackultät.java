import java.util.Scanner;
public class Fuck {
    public static void main (String[] args ){
        Scanner eingabe = new Scanner (System.in);
        int max = eingabe.nextInt();
        eingabe.close();
        int fack = 1;
        while (max > 0){
            fack = fack * max;
            max = max - 1;
        }
    System.out.println(fack);}}