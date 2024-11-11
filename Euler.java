import java.util.Scanner;

public class Euler {
    public static void main (String[] args ){
    Scanner scan = new Scanner(System.in);
    System.out.println("Itteratioen:");
    int itteratioen = scan.nextInt();
    System.out.println("Itteratioen: " + itteratioen + "  Startwert:");
    double startwert = scan.nextDouble();
    System.out.println("Startwert: " + startwert + "  Prozentuale Veränderungen:");
    double prozVer = scan.nextInt();
    prozVer = prozVer*0.01;
    System.out.println("Prozentuale Veränderungen: " + prozVer);
    scan.close();
    for (int i=1; i<= itteratioen; i++){
        startwert = startwert* prozVer;
        System.out.println(i+" " +startwert);
    }}}