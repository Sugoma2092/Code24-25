import java.util.*;
public class Primzahl {

    static Boolean isPrime(long p_can){
        for (int counter = 2; counter * counter <= p_can; counter++) {
            if((p_can % counter)==0){
                return false;}
            }
        return true;
    }

    public static void main (String[] args ){
        Scanner eingabe = new Scanner (System.in);
        long max = eingabe.nextInt();
        eingabe.close();
        List<String> list = new ArrayList<>();
        for (int p_can = 2; p_can <= max; p_can++) {
            if (isPrime(p_can)) {
                list.add(String.valueOf(p_can));
            }
        }
System.out.println(list);}}