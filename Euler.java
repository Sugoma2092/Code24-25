import java.util.Scanner;

public class Euler {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("iterationen:");
        int iterationen = scan.nextInt(); // Eingabe der iterationen
        System.out.println("iterationen: " + iterationen + "  Startwert:");
        double startwert = scan.nextDouble(); // Eingabe des Startwerts
        System.out.println("Startwert: " + startwert + "  Prozentuale Veränderungen:");
        double prozVer = scan.nextInt(); // Eingabe der prozentualen Veränderungen
        prozVer = prozVer * 0.01; // Umwandelung in %
        System.out.println("Prozentuale Veränderungen: " + prozVer);
        scan.close();
        for (int i = 1; i <= iterationen; i++) {
            startwert = startwert * prozVer; // neue Werte
            System.out.println(i + " " + startwert); // Ausgabe
        }
    }
}