import java.util.Scanner;
public class Fakultät {
    public static void main (String[] args ){
        Scanner eingabe = new Scanner (System.in);
        int max = eingabe.nextInt();
        eingabe.close();
        int fakultät= 1;
        while (max > 0){
            fakultät= fakultät* max;
            max = max - 1;
        }
    System.out.println(fakultät);
}}