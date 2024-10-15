import java.util.Scanner;
public class Zahlenrten {
public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
        int Zufallszahl = (int) (101 * Math.random()); //Zahl zwischen 0 und 100 generiert;
        int Vers = 0;
        System.out.println("Zahl zwischen 0 und 100");
        int gerateneZahl = scan.nextInt();
        while (gerateneZahl != Zufallszahl){
        if (gerateneZahl < Zufallszahl){
            System.out.println("Zu klein"); 
            System.out.println("neue Eingabe");
            gerateneZahl = scan.nextInt();
            Vers = Vers + 1;}
        if (gerateneZahl > Zufallszahl){
            System.out.println("Zu Groß"); 
            System.out.println("neue Eingabe");
            gerateneZahl = scan.nextInt();
            Vers = Vers + 1;}}
            System.out.println("Richtig!");
            Vers = Vers + 1;
            System.out.println(Vers+ "Versuche");
            scan.close();
}}