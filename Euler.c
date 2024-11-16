int main()
{
    printf("Iteratioen:\n");
    int iteratioen = 0; // Eingabe der Iteratioen
    scanf("%d",&iteratioen);
    printf("Iteratioen: %d   Startwert:", iteratioen);
    double startwert=0; // Eingabe des Startwerts
    scanf("%lf",&startwert); 
    printf("Startwert: %lf  Prozentuale Veränderungen:\n", startwert);
    double prozVer = 0; // Eingabe der prozentualen Veränderungen
    scanf("%lf", &prozVer);
    prozVer = prozVer * 0.01; // Umwandelung in %
    printf("Prozentuale Veränderungen: %lf\n", prozVer);
    for (int i = 1; i <= iteratioen; i++)
    {
        startwert = startwert * prozVer;  // neue Werte
        printf("%d %lf\n", i, startwert); // Ausgabe
    }
}