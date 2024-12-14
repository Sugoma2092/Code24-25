#needs: odf odfpy pandas
# pip install odf 
# pip install odfpy 
# pip install pandas
import pandas as pd

# Initialize an empty DataFrame to store the data
data = pd.DataFrame(columns=['t', 'x', 'y'])

#Schieberegler
m = 68.1    #Masse in kg
C = 0.8     #Spezieller Luftwiederstandungskoeffizient ((0;2])
A = 60      #Querschnittsfläche in cm³
vel_x = 0.1 #Start X-Geschwindigkeit
vel_y = 0.1 #Start Y-Geschwindigkeit
d_t = 0.01   #Zeitschritt
t_max = 100 #Maximale Zeit

# Konstanten
g = 9.81    #Gravitation
S = 1.29    #Luftdichte

#Initialisierung
x = 0       #Streke in x Richtung in m
y = 0       #Streke in y Richtung in m
t = 0       #Zeitzählvariable
F = g*m     #Anziehung der Kraft der Erde 
a_x = 0     #Besleunigung in x Richtung
a_y = 0     #Besleunigung in y Richtung
Besch_x = 0 
Besch_y = 0 
d_v_x = 0   #Delta Geschwindigkeit in x Richtung
d_v_y = 0   #Delta Geschwindigkeit in y Richtung
v_x = 0     #Geschwindigkeit in x Richtung
v_y = 0     #Geschwindigkeit in y Richtung
d_S_x = 0   #Delta S in x Richtung
d_S_y = 0   #Delta S in Y Richtung

#Bewegung
while t < t_max:

    F_Luft = 0.5*S*A*C #ohne die Geschwindigkeit

    # Bewegung in x-Richtung
    Besch_x += F-((vel_x - g)*F_Luft)   #Beschleunigung in x Richtung
    a_x = Besch_x / m                   #a in x-Richtung
    d_v_x= a_x * d_t                    #Berechnung von Delta V in x Richtung
    v_x +=d_v_x                         #Berechnung der neuen Geschwindigkeit in x Richtung
    d_S_x = v_x * d_t                   #Berechnung von Delta S in x Richtung
    x+=d_S_x                            #Strecke in x Richtung

    # Bewegung in y-Richtung
    Besch_y += F-((vel_y - g)*F_Luft)   #Beschleunigung in y Richtung
    a_y = Besch_y / m                   #a in y Richtung
    d_v_y= a_y * d_t                    #Berechnung von Delta V in y Richtung
    v_y +=d_v_y                         #Berechnung der neuen Geschwindigkeit in y Richtung
    d_S_y = v_y * d_t                   #Berechnung von Delta S in y Richtung
    y+=d_S_y                            #Strecke in y Richtung

    # Ausgabe
    print(f"Zeit:", t, "x:", x, "y:", y)#Output the current position and time

    # Add the current values of t, x, y to the DataFrame
    data = data._append({'t': t, 'x': x, 'y': y}, ignore_index=True)
    t += d_t

# Export the DataFrame to an .ods file
data.to_excel('output.ods', engine='odf', index=False)