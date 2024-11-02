import java.util.Arrays;
import java.util.Scanner;
public class Fibonacci {
    public static void main (String[] args ){
        Scanner eingabe = new Scanner (System.in);
        int max = eingabe.nextInt();
        eingabe.close();
        int m = 3;
        long[] Fibonacci = new long[max];
        if (max >= 1) {
            Fibonacci[0]=1;}
        if (max >= 2) {Fibonacci[1]=2;}
while (max >= m) {
    Fibonacci[(m-1)] = Fibonacci[m-3]+ Fibonacci[(m-2)];
m = m + 1;}
System.out.println(Arrays.toString(Fibonacci));
    }}