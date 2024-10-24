import java.util.Scanner;
public class Taschenrechner {
    public static void main (String[] args ){
        Scanner eingabe = new Scanner (System .in);
        System.out.println("Rechenart 1:a+b 2:a-b 3:a*b 4:a/b 5:a^b");
        int Rechenart = eingabe.nextInt();
        System.out.println("a:");
        int a = eingabe.nextInt();
        System.out.println("b:");
        int b = eingabe.nextInt();
        eingabe.close();
        double Loesung=0;
        if (Rechenart==1){
            Loesung=Plus(a,b);
        }
        else if (Rechenart==2){
            Loesung=Minus(a,b);
        }
        else if (Rechenart==3){
            Loesung=Mal(a,b);
        }
        else if (Rechenart==4){
            Loesung=Geteilt(a,b);
        }
        else if (Rechenart==5){
            Loesung=Hoch(a,b);
        }
        System.out.println("Loesung: " + Loesung);
    }
    public static double Plus(int a,int b){
        double Loesung = 0;
        Loesung = a + b;
        return Loesung;
    }
    public static double Minus(int a,int b){
        double Loesung = 0;
        Loesung = a - b;
        return Loesung;
    }
    public static double Mal(int a,int b){
        double Loesung = 0;
        Loesung = a * b;
        return (Loesung);
    }
    public static double Geteilt(int a,int b){
        double Loesung = 0;
        Loesung = (double) a / b;
        return (Loesung);
    }
    public static double Hoch(int a,int b){
        double Loesung  = 1;
        while(b>=1){
            Loesung = Loesung*a;
            b= b-1;
        }
        return (Loesung);
    }}
