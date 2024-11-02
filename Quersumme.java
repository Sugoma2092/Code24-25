import java.util.Scanner;
public class Quersumme {
    public static void main (String[] args ){
        Scanner eingabe = new Scanner (System.in);
        long max = eingabe.nextInt();
        max = 5;
        eingabe.close();
        long quer = 0;
        long querm = 0;
        long quers = 0;
        while (max > 0){
            quer = max % 10;
            max = (int) (max / 10);
            quers += quer;
            
            if (!(quers < 10)){
            querm = quers % 10;
            quers = (int) (quers / 10);
            quers += querm;
            }}
    System.out.println(quers);
}}